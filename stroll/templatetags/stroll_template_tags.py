from django import template

from stroll.models import *
register = template.Library()

# Creates a walk from its attributes
@register.inclusion_tag('stroll/walk_element.html')
def walk_element(walk, display_type):
    return {"walk": walk, "display_type": display_type}

# Creates a question from its attributes
@register.inclusion_tag('stroll/question_element.html')
def question_element(question):
    return {"question": question}

# Creates a comment from its attributes
@register.inclusion_tag('stroll/comment_element.html')
def comment_element(comment, user, parent):
    return {"comment": comment, "user": user, "parent": parent}

# Creates a comment section from an array some comments
# User need to passed into this
@register.inclusion_tag('stroll/comments_section.html')
def comments_section(comments, user, parent, id):
    return {"comments": comments, "user": user, "parent": parent, 'id': id}

# Helper method to the walk objects accociated with the walk cookies
@register.filter
def get_walks_from_cookie(walk_cookies):

    if walk_cookies == None:
        return []

    # Seperates out the ids
    # The "a" is the seperator used between the cookie ids
    walk_cookies = walk_cookies.split("a")

    # Grabs the walk objects associated with the ids and skips them if the walk was deleted
    return_walks = []
    for walk_id in walk_cookies:
        if walk_id:
            try:
                return_walks.append(Walk.objects.get(id=walk_id))
            except:
                pass
    
    return return_walks