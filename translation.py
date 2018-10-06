import requests
from HandleJs import Py4Js


def removeRedundantSpace(content):
    for _ in range(10):
        content = content.replace('  ', ' ')
    return content


def translate(content, tk):
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return

    param = {'tk': tk, 'q': content}

    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
        &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&
        tsel=0&kc=2""", params=param)

    result_list = result.json()
    with open('translation.txt', 'w', encoding='utf-8') as f:
        for item in result_list[0]:
            if item[0] is None or item[1] is None:
                pass
            else:
                f.write(item[1])
                print(item[1])
                f.write('\n')
                f.write(item[0])
                print(item[0])
                f.write('\n\n')
                print('\n')
        f.write('所有的内容：\n')
        f.write(content)
        f.write('\n')
        for item in result_list[0]:
            if item[0] is None or item[1] is None:
                pass
            else:
                f.write(item[0])
                print(item[0])


def main():
    js = Py4Js()
    print('请输入需要翻译的内容：\n')
    inputStr = input()
    paper = ''
    while inputStr.strip() != '':
        paper = paper + ' ' + inputStr
        inputStr = input()

    paper = paper.replace('\n', ' ')
    paper = paper.replace('', ' ')
    paper = removeRedundantSpace(paper)

    tk = js.getTk(paper)
    translate(paper, tk)
    print('已经保存到translation.txt文件中.\n')


if __name__ == "__main__":
    main()
