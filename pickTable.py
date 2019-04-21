import re
def tableContent(content_html):
    '''
    :param content_html: html_structure data with table
    :return: str
    '''
    article_content = ''
    content_html_list = re.findall(r'(.*?)(<table.*?</table>)',content_html,re.M|re.S)
    for i in content_html_list:
        soup_ordinary = bs(i[0],'html.parser')
        article_content += '\n'.join([ip.getText() for ip in soup_ordinary.find_all('p')]) + '\n'
        table_rows = re.findall(r'<tr>(.*?)</tr>',i[1],re.M|re.S) # 寻找表行<tr>字段
        table_cols =  lambda irow : re.findall(r'<td(.*?)</td>',irow,re.M|re.S) # 寻找表每一行每一列<td>字段
        table_ip = lambda icol : re.findall(r'<p>(.*?)</p>',icol,re.M|re.S) # 获取表每一列下<p>字段
        table_data = ['  |  '.join([''.join(table_ip(icol)) for icol in table_cols(irow)]) for irow in
                      table_rows]  # 遍历 row,col (col间用\t间隔)
        article_content += '-' * 30 + 'TABLE START' + '-'*30 + '\n'
        article_content += '\n'.join(table_data) + '\n' # row 间用 \n 间隔
        article_content += '-' * 30 + 'TABLE END' + '-'*30 + '\n'
    "search html field remainling"
    moreContent = cat(re.search(r'.*</table>(.*)<style>',content_html,re.M|re.S))
    soup_plus = bs(moreContent,'html.parser')
    article_content += '\n'.join([ip.getText() for ip in soup_plus.find_all('p')]) + '\n'
    return article_content
