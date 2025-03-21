from django import template

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
def comment_element(comment):
    return {"comment": comment}

# Creates a comment section from an array some comments
# User need to passed into this
@register.inclusion_tag('stroll/comments_section.html')
def comments_section(comments, user):
    return {"comments": comments, "user": user}
