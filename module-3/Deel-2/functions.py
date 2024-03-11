import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_INN_HUMAN_SILVER_PER_NIGHT,COST_INN_HORSE_COPPER_PER_NIGHT
from math import ceil

##################### O03 #####################

def copper2silver(amount:int) -> float:
    silver_amount = amount * 0.1
    return silver_amount

def silver2gold(amount:int) -> float:
    gold_amount = amount * 0.2
    return  gold_amount



def copper2gold(amount: int) -> float:
    return round(silver2gold( copper2silver(amount)),2)


def platinum2gold(amount:int) -> float:
    platinum_naar_gold = amount * 25
    return platinum_naar_gold

def getPersonCashInGold(personCash:dict) -> float:
    total_gold = 0
   
    total_gold += copper2gold(personCash.get('copper', 0))  
    total_gold += silver2gold(personCash.get('silver', 0))
    total_gold += personCash.get('gold', 0)
    total_gold += platinum2gold(personCash.get('platinum', 0))
    return total_gold  
                                                                                                                                                                    
##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    total_cost_copper = (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS

    total_cost_gold = copper2gold(total_cost_copper)
    return total_cost_gold

##################### O06 #####################

def getFromListByKeyIs(lst: list, key: str, value: any) -> list:
    filtered_list = []
    for item in lst:
        if item.get(key) == value:
            filtered_list.append(item)
    return filtered_list

def getAdventuringPeople(people: list) -> list:
    adventuring_people = []
    for person in people:
        if person.get('adventuring') == True:
            adventuring_people.append(person)
    return adventuring_people

def getShareWithFriends(friends: list) -> list:
    share_with_friends = []
    for friend in friends:
        if friend.get('shareWith') == True:
            share_with_friends.append(friend)
    return share_with_friends

def getAdventuringFriends(friends: list) -> list:
    adventuring_friends = []
    adventuring_people = getAdventuringPeople(friends)
    share_with_friends = getShareWithFriends(friends)
    for friend in adventuring_people:
        if friend in share_with_friends:
            adventuring_friends.append(friend)
    return adventuring_friends

##################### O07 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return ceil(people / 2)

def getNumberOfTentsNeeded(people: int) -> int:
    return ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
    total_cost_horse_silver = (horses * COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS 

    total_cost_tent = (tents * COST_TENT_GOLD_PER_WEEK ) * ceil(JOURNEY_IN_DAYS/7) 

    total_cost = silver2gold(total_cost_horse_silver) + total_cost_tent
    return total_cost

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    items_in_text = []
    for item in items:
        items_in_text.append(f"{item['amount']}{item['unit']} {item['name']}")
    if len(items_in_text) > 1:
        return', '.join(items_in_text[:-1]) +' & '+ items_in_text[-1]
    else:
        return items_in_text[0]

def getItemsValueInGold(items: list) -> float:
    total_value = 0
    for item in items:
        price_amount = item['price']['amount']
        item_amount = item['amount']
        price_type = item['price']['type']

        if price_type == 'copper':
            total_value += copper2gold(price_amount) *  item_amount
        elif price_type == 'silver':
            total_value += silver2gold(price_amount) * item_amount
        elif price_type == 'platinum':
            total_value += platinum2gold(price_amount) * float(item_amount) 
        else:
            total_value += price_amount * item_amount
    return total_value


##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total_gold = 0
    for  person in people:
        preson_cash = person.get('cash', {})
        total_gold += getPersonCashInGold(preson_cash)
    return round(total_gold, 2)

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    interesting_investors = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            interesting_investors.append(investor)
    return interesting_investors

def getAdventuringInvestors(investors:list) -> list:
    interesting_investors = getInterestingInvestors(investors)
    adventurous_investors = []
    for investor in interesting_investors:
        if investor['adventuring']:
            adventurous_investors.append(investor)
    return adventurous_investors

def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    aantal_investors = len(getAdventuringInvestors(investors))
 
    cost_rent = getTotalRentalCost(aantal_investors, aantal_investors )
    food_cost = getJourneyFoodCostsInGold(aantal_investors, aantal_investors)
    gear_cost = getItemsValueInGold(gear) * aantal_investors
 
    return cost_rent + food_cost + gear_cost

##################### O11 #####################


def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    total_nights = 0
    while True:
        cost_in_gold = getJourneyInnCostsInGold(total_nights, people, horses)
        if cost_in_gold > leftoverGold:
            break
        total_nights += 1
    return total_nights - 1
 
def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    total_cost_silver = nightsInInn * COST_INN_HUMAN_SILVER_PER_NIGHT * people
    total_cost_copper = nightsInInn * COST_INN_HORSE_COPPER_PER_NIGHT * horses
    total_cost_gold = copper2gold(total_cost_copper) + silver2gold(total_cost_silver)
    return round(float(total_cost_gold) , 2)

##################### O13 #####################


def getInvestorsCuts(profitGold: float, investors: list) -> list:
    interesting_investors = getInterestingInvestors(investors)
    investors_cuts = []
 
    for investor in interesting_investors:
        investors_cuts.append(round(investor['profitReturn'] / 100 * profitGold, 2 ))
 
    return investors_cuts
 
 
def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    total_investors_cut = sum(investorsCuts)
    if profitGold > 0 :
        adventurer_cut = profitGold - total_investors_cut
        return round(adventurer_cut / fellowship ,2)
    else:
        return 0.0

##################### O14 #####################

def getEarnigs(profitGold: float, mainCharacter: dict, friends: list, investors: list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # Haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, interestingInvestors)

    # Bepaal het totaal aantal mensen dat deelnam aan het avontuur
    totalParticipants = len(adventuringFriends) + len(adventuringInvestors) + 1  # mainCharacter

    # Verdeel de uitkomsten
    for person in people:
        name = person['name']
        start = getCashInGoldFromPeople([person])
        end = start

        if person in adventuringFriends or person in adventuringInvestors or person == mainCharacter:
            goldCut = getAdventurerCut(profitGold, investorsCuts, totalParticipants)
            end += goldCut
            if person != mainCharacter:
                # Iedereen die deelnam geeft 10 goud aan de avonturier
                end -= 10


        earnings.append({
            'name': name,
            'start': round(start, 2),
            'end': round(end, 2)
        })
    return earnings

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()



    