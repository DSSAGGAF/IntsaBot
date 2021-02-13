from instabot import Bot
import urllib.request
import requests


import time

DELAY = 60
count = 0


def main():
    global count
    bot = Bot(message_delay=5)
    bot.login(
        username="",
        password="",
        use_cookie=True,
        cookie_fname="config\\myCookie.json",
    )
    while True:
        ok = bot.get_messages()
        # print(messages)
        if not ok:
            raise ValueError("failed to get activity")
        messages = bot.api.last_json
        # print(messages["inbox"])
        for thread in messages["inbox"]["threads"]:
            # print(thread["items"])
            for item in thread["items"]:
                # print(item["item_type"])
                # print(item)
                try:
                    if item["item_type"] == "media_share":
                        # print(item)
                        if item["media_share"]["media_type"] == 8:
                            for media in item["media_share"]["carousel_media"]:
                                if media["media_type"] == 2:
                                    urllib.request.urlretrieve(
                                        media["video_versions"][0]["url"],
                                        filename="UsersData\\"+str(item["user_id"])  + " test.mp4",
                                    )
                                    files = {
                                        "file": open(
                                            "UsersData\\"+str(item["user_id"])  + " test.mp4", "rb"
                                        ),
                                    }
                                    response = requests.post("https://file.io", files=files)
                                    json_data = response.json()
                                    bot.send_message(
                                        json_data["link"], str(item["user_id"])
                                    )
                                    bot.send_message(
                                        "please copy the link and use it in Safri Then download it. Thank you for using me :D",
                                        str(item["user_id"]),
                                    )
                                    count = count + 1
                                else:
                                    bot.send_message(
                                        "You can screanshot the post :D", str(item["user_id"])
                                    )
                                    count = count + 1

                        elif item["media_share"]["media_type"] == 2:
                            video = item["media_share"]["video_versions"][0]
                            urllib.request.urlretrieve(
                                video["url"], filename="UsersData\\"+str(item["user_id"])  + " test.mp4"
                            )
                            files = {
                                "file": open("UsersData\\"+str(item["user_id"])  + " test.mp4", "rb"),
                            }
                            response = requests.post("https://file.io", files=files)
                            json_data = response.json()
                            bot.send_message(json_data["link"], str(item["user_id"]))
                            bot.send_message(
                                "please copy the link and use it in Safri Then downloaded Thank you for using me :D",
                                str(item["user_id"]),
                            )
                            count = count + 1

                        else:
                            bot.send_message(
                                "You can screanshot the post :D", str(item["user_id"])
                            )
                            count = count + 1

                    elif item["item_type"] == "story_share":
                        # print(item)
                        try:
                            if (item["story_share"]["media"]["media_type"]==1):
                                pic = item["story_share"]["media"]["image_versions2"]["candidates"][0]
                                urllib.request.urlretrieve(
                                    pic["url"], filename="UsersData\\"+str(item["user_id"])  + " test.jpg"
                                )
                                files = {
                                    "file": open("UsersData\\"+str(item["user_id"])  + " test.jpg", "rb"),
                                }
                                response = requests.post("https://file.io", files=files)
                                json_data = response.json()
                                bot.send_message(json_data["link"], str(item["user_id"]))
                                bot.send_message(
                                    "please copy the link and use it in Safri and Thank you for using me :D",
                                    str(item["user_id"]),
                                )
                                count = count + 1
                            elif (item["story_share"]["media"]["media_type"]==2):
                                video = item["story_share"]["media"]["video_versions"][0]
                                urllib.request.urlretrieve(
                                    video["url"], filename="UsersData\\"+str(item["user_id"])  + " test.mp4"
                                )
                                files = {
                                    "file": open("UsersData\\"+str(item["user_id"])  + " test.mp4", "rb"),
                                }
                                response = requests.post("https://file.io", files=files)
                                json_data = response.json()
                                bot.send_message(json_data["link"], str(item["user_id"]))
                                bot.send_message(
                                    "please copy the link and use it in Safri and Thank you for using me :D",
                                    str(item["user_id"]),
                                )
                                count = count + 1
                        except:
                            bot.send_message(
                            "Sorry I acnt help you with that :|", str(item["user_id"])
                        )

                    elif item["item_type"] == "felix_share":
                        # print(item)
                        if (item["felix_share"]["video"]["media_type"]==1):
                            video = item["felix_share"]["video"]["video_versions"][0]
                            urllib.request.urlretrieve(
                                video["url"], filename="UsersData\\"+str(item["user_id"])  + " test.mp4"
                            )
                            files = {
                                "file": open("UsersData\\"+str(item["user_id"])  + " test.mp4", "rb"),
                            }
                            response = requests.post("https://file.io", files=files)
                            json_data = response.json()
                            bot.send_message(json_data["link"], str(item["user_id"]))
                            bot.send_message(
                                "please copy the link and use it in Safri and Thank you for using me :D",
                                str(item["user_id"]),
                            )
                            count = count + 1
                        else:
                            bot.send_message(
                            "Sorry I acnt help you with that :|", str(item["user_id"])
                        )    

                    elif item["item_type"] == "profile":
                        # print(item)
                        pic = item["profile"]
                        urllib.request.urlretrieve(
                            pic["profile_pic_url"],
                        filename="UsersData\\"+str(item["user_id"]) + " test.jpg"
                        )
                        files = {
                            "file": open("UsersData\\"+str(item["user_id"]) + " test.jpg", "rb"),
                        }
                        response = requests.post("https://file.io", files=files)
                        json_data = response.json()
                        bot.send_message(json_data["link"], str(item["user_id"]))
                        bot.send_message(
                            "please copy the link and use it in Safri Then downloaded Thank you for using me :D",
                            str(item["user_id"]),
                        )
                        count = count + 1

                    elif item["item_type"] == "text":
                        print("Nothing to do")

                    else:
                        count = count + 1
                        bot.send_message(
                            "Sorry I acnt help you with that :|", str(item["user_id"])
                        )
                except:
                        bot.send_message(
                        "Sorry I acnt help you with that :|", str(item["user_id"])
                    )    
        print("done " + str(count))
        time.sleep(DELAY)


if __name__ == "__main__":
    main()