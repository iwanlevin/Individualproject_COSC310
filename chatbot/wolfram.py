import wolframalpha as wa

def define(query):
    question = "Question: "
    app_id = "E3P3GA-3LGTR8XRKR"
    client = wa.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    print(answer)
    definition = ""
    return definition