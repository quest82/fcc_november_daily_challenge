def image_search(images, term):
    result = [x for x in images if term.lower() in x.lower()]

    return result

print(image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG"))