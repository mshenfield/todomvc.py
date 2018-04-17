import attr

@attr.s
class Thing:
    thing = attr.ib()


mything = Thing('sports')
yourthing = Thing('music')

print(mything)
print(yourthing)
