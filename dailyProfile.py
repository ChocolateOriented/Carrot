import datetime
import json

# 设计思路, 怎么好用怎么来, 尽可能符合实际需求

itermFullScore = 5


def evaluate(purposes):
  print("各项满分" + str(itermFullScore) + ", 请对自己做出评价\n")
  aggregateScore = 0;
  fullScore = 0;

  record = {"日期":datetime.datetime.now().strftime("%Y-%m-%d")};
  for purpose in purposes:
    name = purpose["name"]
    weight = purpose["weight"]
    score = int(input(name + ":"))
    score = validaScore(score)

    record[name] = score
    score = (score / itermFullScore) * weight
    aggregateScore += score
    fullScore += weight

  averageScore = aggregateScore / fullScore
  record["总分"] = averageScore
  # 记录评分
  awardUrl = "data/record.json"
  with open(awardUrl,"r",encoding="utf-8") as recordFr:
    records = json.load(recordFr)
    records.append(record)
    with open(awardUrl,"w",encoding="utf-8") as recordFw:
      json.dump(records,recordFw,indent=2,ensure_ascii=False)
  return averageScore


def validaScore(score):
  if (score < 0 or score > itermFullScore):
    return validaScore(int(input("请输入有效分数:")))
  else:
    return score

def getPurposeByType (allPurpose, type):
  todayPurpose = []
  for purpose in allPurpose:
    plans = purpose["plan"]
    for plan in plans:
      if (plan["type"] == type):
        todayPurpose.append(purpose)
  return todayPurpose

print("培养执行力，不要被本能支配, 增加自我奖惩机制")
print("机制说明:")
print("  1. 按事情重要程度加权算分, 总分作为百分比获得娱乐时间, 完成目标, 或满意即可满分")
print("  2. 奖励40/天冲动消费, 完成85%即可获取全部, 未达到60%则无奖励\n")

now = datetime.datetime.now()
purposeUrl = "data/purpose.json"

with open(purposeUrl, 'r',encoding="utf-8") as purposeF:
  allPurpose = json.load(purposeF)

# 工作日
if (now.isoweekday()):
  planType = "workday"
else:  # 周末
  planType = "holiday"

todayPurpose = getPurposeByType(allPurpose,planType)
score = evaluate(todayPurpose)
floor = 0.6
ceiling = 0.85

print("\n得分"+str(score))
if (score<floor):
  input(", 低于"+str(floor)+"无奖励")
elif (score<ceiling):
  incrementalAward = int(score*40)
else:
  incrementalAward = 40
print("获得奖励"+str(incrementalAward))

awardUrl = "data/award.json"
with open(awardUrl,"r",encoding="utf-8") as awardFr:
  previousAward = int(json.load(awardFr))
  currentAward = previousAward + incrementalAward
  with open(awardUrl,"w",encoding="utf-8") as awardFw:
    json.dump(currentAward, awardFw)

input("奖励从"+str(previousAward)+"增加至"+str(currentAward))

