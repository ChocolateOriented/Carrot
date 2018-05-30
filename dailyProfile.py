from plan import *
import datetime

# 设计思路, 怎么好用怎么来, 尽可能符合实际需求

itermFullScore = 5


def evaluate(purposes):
  print("各项满分" + str(itermFullScore) + ", 请对自己做出评价\n")
  aggregateScore = 0;
  fullScore = 0;
  for purpose in purposes:
    score = int(input(purpose.name + ":"))
    score = validaScore(score)
    score = (score / itermFullScore) * purpose.weight
    aggregateScore += score
    fullScore += purpose.weight
  return aggregateScore / fullScore


def validaScore(score):
  if (score < 0 or score > itermFullScore):
    return validaScore(int(input("请输入有效分数:")))
  else:
    return score


print("怠惰时要有按计划行动的执行力，不要被本能支配, 增加自我奖惩机制, 秉承先完成目标, 后接受惩罚, 最后获取奖励")
print("机制说明:")
print("  1. 难以停下的东西作为激励(游戏, 视频等娱乐), 对难以开始的事情做激励")
print("  2. 按事情重要程度加权算分, 总分作为百分比获得娱乐时间, 完成目标, 或满意即可满分")
print("  3. 按评分计算娱乐时间, 空余时间用于补足失分项\n")

now = datetime.datetime.now()

todayPurpose = []
# 工作日
if (now.isoweekday()):
  todayPurpose.append(Purpose("英语", "早上", 20, "单词及新闻"))
  todayPurpose.append(Purpose("机器学习或工作", "下午", 40))
  todayPurpose.append(Purpose("锻炼", "晚饭前", 20))
  todayPurpose.append(Purpose("自由学习", "地铁晚饭后", 10))
  todayPurpose.append(Purpose("睡觉", "11:30左右", 10))
  award = Award("娱乐", 150, datetime.datetime(day=now.day, month=now.month,
                                             year=now.year, hour=21))
else:  # 周末
  todayPurpose.append(Purpose("英语", "早饭后", 20))
  todayPurpose.append(Purpose("锻炼", "英语后", 20))
  todayPurpose.append(Purpose("自由学习", "锻炼后至1:30", 40))
  todayPurpose.append(Purpose("按时睡觉", "12点前", 20))
  award = Award("娱乐", 600,datetime.datetime(day=now.day, month=now.month,
                                            year=now.year, hour=13, minute=30))
score = evaluate(todayPurpose)
punish = int(award.amount * (1 - score))
print("\n得分"+str(score)+", 需减少" + award.name + str(punish)+"分钟, 请补足失分项至"+ (
  award.startTime +
      datetime.timedelta(minutes=punish)).strftime("%H:%M") )

