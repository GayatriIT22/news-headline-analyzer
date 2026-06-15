# Creating a List of Headlines
headlines=['Breaking News: Python Takes Over the World', 'New Study Shows Benefits of Coffee',
           'Tech Giants Announce New AI Innovations', 'Sports Update: Local Team Wins Championship',
           'Health Tips: How to Stay Fit During Winter', 'Entertainment: Upcoming Movie Releases',
           'Travel Guide: Top Destinations for 2024', 'Finance: Stock Market Hits Record Highs',
           'Education: New Trends in Online Learning', 'Environment: Climate Change Initiatives Gain Momentum',
           'Python Is the Most Popular Programming Language in 2024','AI and Python Dominate the Tech World',
           'Coffee Consumption Linked to Improved Health Outcomes', 'Local Team Wins Championship After Intense Match',
        ]

# Categorizing Headlines
categories={ 'Technology':{'tech','ai','python','innovation','programming'},
              'Food':{'food','coffee','cuisine','recipes'},
             'Health':{'health','fitness','wellness'},
             'Entertainment':{'entertainment','movies','music','celebrities'},
             'Travel':{'travel','destinations','tourism'},
                'Finance':{'finance','stock','market','economy'}, 
                'Education':{'education','online','learning','trends'},
                'Environment':{'environment','climate','change','sustainability'},
                'Sports': {'sports', 'team', 'wins', 'championship', 'tournament'}
                }



# CLassifying Headlines
headline_category = dict()
category_count=dict()
for headline in headlines:
    headline_lower=headline.lower()
    words=headline_lower.replace(':',' ').replace(',',' ').split() 
    found = False
    for category, keywords in categories.items():
        for word in words:
            if word in keywords:
                category_count[category] = category_count.get(category, 0) + 1
                found = True
                headline_category[headline] = category
                break
        if found:
            break    
    if not found:
        pass
    
# Counting Word Frequencies
stop_words={'the','is','and','of','to','in','a','for','on','with','as','by','that','from'}
count=dict()
for headline in headlines:
    healine_lower=headline.lower()
    words=healine_lower.replace(':',' ').replace(',',' ').split() 
    for word in words:
        if word not in stop_words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
sorted_words=[]
for word, freq in count.items():
    sorted_words.append((word, freq))
sorted_words.sort(reverse=True)
Top_N_words=sorted_words[:5]
for word, freq in Top_N_words:
    pass
    

# Identifying Similar Headlines 
similar_pairs = []
for i in range(len(headlines)):
    for j in range(i + 1, len(headlines)):   # j starts after i, never repeats
        headline1 = headlines[i]
        headline2 = headlines[j]
        words1 = set(headline1.lower().replace(':', ' ').replace(',', ' ').split())
        words2 = set(headline2.lower().replace(':', ' ').replace(',', ' ').split())
        common_words = words1.intersection(words2)
        if len(common_words) > 2:
            similar_pairs.append((headline1, headline2, common_words))
most_covered = max(category_count, key=category_count.get)


# Menu
while True:
    print("*"*45)
    print(f"{'*'*10} NEWS HEADLINE ANALYZER {'*'*10}")
    print("*"*45)
    print("  1. Show all categories")
    print("  2. Top 5 frequent words")
    print("  3. Similar headlines")
    print("  4. Search by keyword")
    print("  5. Categorise my headline")
    print("  6. Most covered topic")
    print("  7. Exit")
    print("*"*45)

    choice = input("\n  Enter your choice (1-7): ").strip()

    if choice == '1':
        print("\n📰 NEWS SUMMARY:")
        for category in categories.keys():
            print(f"\n  {category} - {category_count.get(category, 0)} headlines")
            for headline, cat in headline_category.items():
                if cat == category:
                    print(f"    - {headline}")

    elif choice == '2':
        print("\n📊 TOP 5 MOST FREQUENT WORDS:")
        for word, freq in Top_N_words:
            print(f"  '{word}' appeared {freq} times")

    elif choice == '3':
        print("\n⚠️  SIMILAR HEADLINES:")
        if similar_pairs:
            for h1, h2, common in similar_pairs:
                print(f"\n  '{h1}'")
                print(f"  '{h2}'")
                print(f"  Common words: {common}")
        else:
            print("  No similar headlines found.")

    elif choice == '4':
        keyword = input("\n  Enter keyword to search: ").lower().strip()
        found_category = None
        for category, keywords in categories.items():
            if keyword in keywords:
                found_category = category
                break
        related_headlines = [h for h in headlines if keyword in h.lower()]
        print(f"\n🔍 Results for '{keyword}':")
        print("━" * 40)
        if found_category:
            print(f"  📁 Category: {found_category} ({category_count.get(found_category, 0)} headlines)")
            for headline, cat in headline_category.items():
                if cat == found_category:
                    print(f"    - {headline}")
        if related_headlines:
            print(f"\n  📰 Headlines containing '{keyword}':")
            for h in related_headlines:
                print(f"    - {h}")
        if keyword in count:
            print(f"\n  📈 '{keyword}' appears {count[keyword]} times")
        if not found_category and not related_headlines:
            print("  ❌ No results found.")

    elif choice == '5':
        news = input("\n  Enter your headline: ").lower().strip()
        news_words = news.replace(':', ' ').replace(',', ' ').split()
        found = False
        for category, keywords in categories.items():
            for word in news_words:
                if word in keywords:
                    print(f"\n  ✅ Category: {category}")
                    found = True
                    break
            if found:
                break
        if not found:
            print("\n  ❌ Unknown category.")

    elif choice == '6':
        print(f"\n🏆 Most covered topic: {most_covered} ({category_count[most_covered]} headlines)")

    elif choice == '7':
        print("\n ✨ Thank you for using the NEWS HEADLINE ANALYZER!  ✨")
        break

    else:
        print("\n  ❌ Invalid choice. Enter 1-7.")