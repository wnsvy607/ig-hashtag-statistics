import ig_api as ig


token = ig.get_token("384665817518599", "1aafc55e63ddf20d8fcc4cd4cd646d7f")
print(token)
temp = "EAAFd2f1pEgcBO2sDZBBesBDpMdqW4tUWJD3bUSzxtTD5nO0HDmLZCCa9TVcAPUtWjaxZARPE8pIvY6uu8MGX6zIPkww8lXs2mOhxOHVRWXAHP3Vl79jto82s95FRywFBudRHm6FZBy8v7I9s2CEonb3Y2BpCM1RoL5nd6YUZBN1BFbnCNchhsPJOMaln5LaC9TRU69GDQ49178GzDtgZDZD"
acc = ig.get_account(temp, "2551922211648157")
print(acc)
