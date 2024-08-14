from django.shortcuts import render

def richest_people(request):
    people = [
{
    "name": "Elon Musk",
    "net_worth": "$245 billion",
    "business": "Tesla, SpaceX",
    "contributions": "Electric vehicles, space exploration",
    "intro": "Elon Musk is the CEO of Tesla and SpaceX, pioneering electric vehicles and space travel."
},
{
    "name": "Jeff Bezos",
    "net_worth": "$165 billion",
    "business": "Amazon",
    "contributions": "E-commerce, cloud computing",
    "intro": "Jeff Bezos founded Amazon, revolutionizing global e-commerce and cloud computing."
},
{
    "name": "Bernard Arnault",
    "net_worth": "$190 billion",
    "business": "LVMH",
    "contributions": "Luxury goods",
    "intro": "Bernard Arnault is the CEO of LVMH, overseeing prestigious luxury brands like Louis Vuitton and Dior."
},
{
    "name": "Bill Gates",
    "net_worth": "$114 billion",
    "business": "Microsoft",
    "contributions": "Software development, philanthropy",
    "intro": "Bill Gates co-founded Microsoft, leading advancements in software and global philanthropy."
},
{
    "name": "Warren Buffett",
    "net_worth": "$106 billion",
    "business": "Berkshire Hathaway",
    "contributions": "Investment, philanthropy",
    "intro": "Warren Buffett is the CEO of Berkshire Hathaway and is renowned for his investment acumen."
},
{
    "name": "Larry Ellison",
    "net_worth": "$128 billion",
    "business": "Oracle",
    "contributions": "Database software, cloud computing",
    "intro": "Larry Ellison co-founded Oracle, leading the way in database software and cloud services."
},
{
    "name": "Larry Page",
    "net_worth": "$110 billion",
    "business": "Google",
    "contributions": "Search engines, technology",
    "intro": "Larry Page is a co-founder of Google, instrumental in the development of modern internet search."
},
{
    "name": "Sergey Brin",
    "net_worth": "$105 billion",
    "business": "Google",
    "contributions": "Search engines, technology",
    "intro": "Sergey Brin co-founded Google, playing a key role in the evolution of internet search technology."
},
{
    "name": "Mukesh Ambani",
    "net_worth": "$97 billion",
    "business": "Reliance Industries",
    "contributions": "Telecommunications, petrochemicals",
    "intro": "Mukesh Ambani is the chairman of Reliance Industries, a leader in telecommunications and energy."
},
{
    "name": "Steve Ballmer",
    "net_worth": "$100 billion",
    "business": "Microsoft, Los Angeles Clippers",
    "contributions": "Software development, sports management",
    "intro": "Steve Ballmer is the former CEO of Microsoft and current owner of the Los Angeles Clippers NBA team."
}

        # Add more people similarly
    ]
    return render(request, 'richest_people.html', {'people': people})

