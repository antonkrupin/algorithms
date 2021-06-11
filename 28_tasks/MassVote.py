def MassVote(n,votes):
    allVotes = 0
    votesPercents = []
    maxVotesPercent = 0
    if(n == 1):
        return ('majority winner 1')
    else:
        for x in range(len(votes)):
            allVotes += votes[x]
        
        for x in range(len(votes)):
            votesPercents.append(round((votes[x]/allVotes)*100,3))
        
        maxVotesPercent = max(votesPercents)
        
        counter = 0
        for x in range(len(votesPercents)):
            if(maxVotesPercent == votesPercents[x]):
                counter += 1
        
        if(counter == 1):
            index = 0
            for x in range(len(votesPercents)):
                if(votesPercents[x] == maxVotesPercent):
                    index = x + 1
            if(maxVotesPercent > 50):
                return ('majority winner %s' % index)
            if(maxVotesPercent <= 50):
                return ('minority winner %s' % index)
        else:
            return ('no winner')
