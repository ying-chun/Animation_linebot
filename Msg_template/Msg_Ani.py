from linebot.models import *

##觀看網址button
def get_link_box(web, url):
    links = []
    for i in range(len(web)):
        link = {
                "type": "button",
                "action": {
                            "type": "uri",
                            "label": web[i],
                            "uri": url[i]
                },
                "height": "sm"
        }
        links.append(link)
    return links


##收藏判斷
def ani_collect(collect , AniName):
    if collect == True:
        content = {
            "type": "button",
            "action": {
            "type": "message",
            "label": "已收藏",
            "text": "取消收藏" + AniName
            },
            "style": "primary",
            "color": "#F4A7B9",
            "height": "sm"
        }
    elif collect == False:
        content = {
            "type": "button",
            "action": {
            "type": "message",
            "label": "收藏",
            "text": "收藏" + AniName
            },
            "style": "primary",
            "color": "#81C7D4",
            "height": "sm"
        }
    return content


##動畫bubble
def ani_bubble(name, intro, image, tag, tag_color, links, collect):
    Ani = {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "image",
                    "url": image,
                    "size": "full",
                    "aspectRatio": "1.54:1",
                    "aspectMode": "cover"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": tag,
                        "size": "xs",
                        "align": "center",
                        "gravity": "center",
                        "color": "#ffffff"
                    }
                    ],
                    "backgroundColor": tag_color,
                    "position": "absolute",
                    "offsetStart": "15px",
                    "offsetTop": "15px",
                    "cornerRadius": "100px",
                    "height": "25px",
                    "paddingStart": "md",
                    "paddingEnd": "md"
                }
                ]
            }
            ],
            "paddingAll": "0px"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": name,
                "weight": "bold",
                "size": "lg",
                "wrap": True
            },
            {
                "type": "text",
                "text": intro,
                "wrap": True,
                "margin": "md",
                "size": "xs",
                "color": "#666666"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": links,
                    "paddingTop": "sm"
                }
                ]
            }
            ],
            "paddingBottom": "none"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [collect],
            "paddingTop": "none"
        }
    }
    return Ani


##動畫選擇 #quickly reply
def ani_name_select(AniName_list):
    QuickReplyButtons = []
    for ani in AniName_list:
        QuickReplyButtons.append(
            QuickReplyButton(
                action=MessageAction(
                    label = ani, 
                    text = "#" + ani
                )
            )
        )

    text_message = TextSendMessage(
                text = "請選擇您欲查詢的動漫" ,
                quick_reply = QuickReply(items = QuickReplyButtons)
    )
    return text_message


##動畫資訊 #圖文選單
def ani_information(AniData, inDB): 
    name = AniData[0]
    intro = AniData[1]
    image = AniData[2] 
    tag =  AniData[3]
    tag_color = AniData[4]
    links = get_link_box(AniData[5], AniData[6])
    collect = ani_collect(inDB , name)

    content = ani_bubble(name, intro, image, tag, tag_color, links, collect)
    flex_message = FlexSendMessage(
            alt_text = name + "資訊",
            contents = content
    )
    return flex_message


##星期資訊 #多頁訊息
def ani_week(AniWeek, AniData, inDB): 
    name = AniData[0]
    intro = AniData[1]
    image = AniData[2] 
    tag =  AniData[3]
    tag_color = AniData[4]
    web = AniData[5]
    url = AniData[6]

    ani_bubbles = []
    for i in range(len(name)):
        links = get_link_box(web[i], url[i])
        collect = ani_collect(inDB[i] , name[i])
        ani_bubbles.append(ani_bubble(name[i], intro[i], image[i], tag[i], tag_color[i] ,links, collect))

    flex_message = FlexSendMessage(
            alt_text = "星期" + AniWeek + "番劇資訊",
            contents = {
                        "type": "carousel",
                        "contents": ani_bubbles
            }
    )
    return flex_message


#類別資訊 ＃多頁訊息
def ani_category(AniCate, AniData, inDB): 
    name = AniData[0]
    intro = AniData[1]
    image = AniData[2] 
    tag =  AniData[3]
    tag_color = AniData[4]
    web = AniData[5]
    url = AniData[6]

    ani_bubbles = []
    for i in range(len(name)):
        links = get_link_box(web[i], url[i])
        collect = ani_collect(inDB[i] , name[i])
        ani_bubbles.append(ani_bubble(name[i], intro[i], image[i], tag[i], tag_color[i] ,links, collect))

    flex_message = FlexSendMessage(
            alt_text = AniCate + "番劇資訊",
            contents = {
                        "type": "carousel",
                        "contents": ani_bubbles
            }
    )
    return flex_message