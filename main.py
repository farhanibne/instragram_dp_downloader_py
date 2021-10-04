import instaloader
ig = instaloader.Instaloader()
profile = input("Enter A UserName : ")
ig.download_profile(profile,profile_pic_only=True)
