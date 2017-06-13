import json
#문자열에서 문자하나 카운트 해주는 모듈
class Ccfs():
    def __init__(self, sentense, character):

        if(len(character)!=1):
            self.count = -1
        else:
            self.count = sentense.count(character)

        self.length = len(sentense)
    def getJson(self):
        return json.dumps({"count":self.count,"length":self.length})

if __name__ == "__main__":
    #test
    print(Ccfs("ashjjjjjs salsl    ","s").getJson())