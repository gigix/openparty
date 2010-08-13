# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed

from apps.core.models import Event, Topic

class Events_Feed(Feed):

    title = "Beijing OpenParty 最新活动列表"
    link = "/events"
    description = "发布 Beijing OpenParty 的最新活动信息"

    def items(self):
        return Event.objects.order_by('-begin_time')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description

class Topics_Feed(Feed):

    title = "Beijing OpenParty 最新话题列表"
    link = "/topics"
    description = "发布 Beijing OpenParty 的最新活动中的话题信息"

    def items(self):
        return Topic.objects.all().order_by('-in_event__begin_time','-accepted', '-total_votes')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description
