### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # double equal sign missing
      return True
    else # colon is missing
      return False
   

  dif highest_card(self, card1 card2): # 'def' instead of 'dif' should be used as well as coma after should separate 'card1' and 'card2'
  if card1.value > card2.value:
    return card # 'card1' instead of 'card' should be used
  else:
    return card2
  # line 28, 29, 30 and 31 require indentation


def cards_total(self, cards):
  total # 'total' should be equal 0 ('= 0' is missing)
  for card in cards:
    total += card.value
    return "You have a total of" + total # space could be added before the end of the string "You have a total of"
    # string interpolation of 'total' is missing(f"{total}").
  #line 35, 36, 37 and 38 require indentation
```
