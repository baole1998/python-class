def format_money(money):
    money_int = int(money)
    money_bil = money_int // 1000000000
    money_mil = (money_int - money_bil * 1000000000) // 1000000
    money_thousand = (money_int - money_bil * 1000000000 - money_mil * 1000000) // 1000

    money_text = ""
    if money_bil > 0:
        money_text = money_text + str(money_bil) + "."
        if money_mil > 100:
            money_text = money_text + str(money_mil) + "."
        elif money_mil > 10:
            money_text = money_text + "0" + str(money_mil) + "."
        elif money_mil > 0:
            money_text = money_text + "00" + str(money_mil) + "."
        else:
            if money_bil > 0:
                money_text = money_text + "000."

    else:
        if money_mil > 0:
            money_text = money_text + str(money_mil) + "."
        else:
            pass

    if money_bil > 0 or money_mil > 0:
        if money_thousand > 100:
            money_text = money_text + str(money_thousand) + ".000"
        elif money_thousand > 10:
            money_text = money_text + "0" + str(money_thousand) + ".000"
        elif money_thousand > 0:
            money_text = money_text + "00" + str(money_thousand) + ".000"
        else:
            money_text = money_text + "000.000"
    else:
        if money_thousand > 0:
            money_text = money_text + str(money_thousand) + ".000"
        else:
            money_text = str(money_int)

    return money_text
