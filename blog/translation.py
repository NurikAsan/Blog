from modeltranslation.translator import register, TranslationOptions

from .models import Post, Comment


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'slug',
        'body',
        'publish'
    )


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'email',
        'body',
    )
