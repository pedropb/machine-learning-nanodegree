p_chris = 0.5
p_sarah = 0.5

p_words =  {"chris": {"love": .1, "deal": .8, "life": .1},
            "sarah": {"love": .5, "deal": .2, "life": .3}}

p_joint_chris_love_deal = p_chris * p_words["chris"]["love"] * p_words["chris"]["deal"]
p_joint_sarah_love_deal = p_sarah * p_words["sarah"]["love"] * p_words["sarah"]["deal"] 

p_love_deal = p_joint_chris_love_deal + p_joint_sarah_love_deal
              

p_chris_love_deal = p_joint_chris_love_deal / p_love_deal
p_sarah_love_deal = p_joint_sarah_love_deal / p_love_deal

print "P(CHRIS|\"Love deal\")", p_chris_love_deal
print "P(SARAH|\"Love deal\")", p_sarah_love_deal