

artlist = [
    {"keywords": [
                        {
                            "name": "organizations",
                            "value": "Reddit Inc",
                            "rank": 1,
                            "major": "N"
                        },
                        {
                            "name": "subject",
                            "value": "Banking and Financial Institutions",
                            "rank": 2,
                            "major": "N"
                        },
                        {
                            "name": "organizations",
                            "value": "GameStop Corporation",
                            "rank": 3,
                            "major": "N"
                        },
                        {
                            "name": "organizations",
                            "value": "Citadel Investment Group",
                            "rank": 4,
                            "major": "N"
                        }
                    ]},
    {"keywords": [
        {
            "name": "organizations",
            "value": "GameStop Corporation",
            "rank": 1,
            "major": "N"
        },
        {
            "name": "organizations",
            "value": "Reddit Inc",
            "rank": 2,
            "major": "N"
        },
        {
            "name": "persons",
            "value": "Gill, Keith (1986- )",
            "rank": 3,
            "major": "N"
        },
        {
            "name": "organizations",
            "value": "House Committee on Financial Services",
            "rank": 4,
            "major": "N"
        },
        {
            "name": "subject",
            "value": "Stocks and Bonds",
            "rank": 5,
            "major": "N"
        },
        {
            "name": "subject",
            "value": "Short Selling",
            "rank": 6,
            "major": "N"
        }
    ]}
]

keywords_l = []
for x in artlist:
    tuple_list = []
    count = x["keywords"]
    for y in count:
        tuple_list.append(y["value"])
    keywords_l.append(tuple(tuple_list))

print("done")



