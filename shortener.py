import random
import string
import database_url


orig_url=input("Enter the URL that you want to shorten: ")
base_url, sep, tail=orig_url.partition(".com/")
validate=True

if sep!=".com/":
    print("You didn't pass an valid URL")
    validate=False

def automatic_or_own():
    decision=input("You want that the shortened URL is created automatically (Y) or do you want to stablish your own (N): ").lower()

    if decision=="y":
        lettersNdigits=string.ascii_letters+string.digits
        new_random=""
        for i in range(5):
            new_random=new_random+random.choice(lettersNdigits)

        new_url=base_url+sep+new_random
        print('Your url is: ', new_url)
        return(new_url)

    elif decision=="n":
        own_url=input("Enter the shortener that you want to use in your URL. 'Example: MyUrl will create url.com/MyUrl': ")
        new_url=base_url+sep+own_url
        print('Your url is: ', new_url)
        return(new_url)

new_url=automatic_or_own()
if validate==True:
    database_url.insert(orig_url,new_url)
