from django.conf.urls import patterns, url, include
from django.conf.urls.i18n import i18n_patterns

from django_downloadview import ObjectDownloadView

from contactos.views import ToggleContactEnabledView
from mailit.views import MailitTemplateUpdateView
from nuntium.models import AnswerAttachment
from nuntium.views import (
    ConfirmView,
    MessageThreadView,
    MessageThreadsView,
    MessagesFromPersonView,
    MessagesPerPersonView,
    PerInstanceSearchView,
    WriteMessageView,
    WriteSignView,
    WriteItInstanceDetailView,
    )
from nuntium.user_section.views import (
    AcceptMessageView,
    AcceptModerationView,
    AnswerCreateView,
    AnswerUpdateView,
    ConfirmationTemplateUpdateView,
    MessageDetail,
    MessagesPerWriteItInstance,
    NewAnswerNotificationTemplateUpdateView,
    WriteItDeleteView,
    WriteItInstanceAdvancedUpdateView,
    WriteItInstanceAnswerNotificationView,
    WriteItInstanceApiAutoconfirmView,
    WriteItInstanceApiDocsView,
    WriteItInstanceContactDetailView,
    WriteItInstanceModerationView,
    WriteItInstanceMaxRecipientsView,
    WriteItInstanceRateLimiterView,
    WriteItInstanceStatusView,
    WriteItInstanceTemplateUpdateView,
    WriteItInstanceUpdateView,
    WriteItInstanceWebBasedView,
    WriteitPopitRelatingView,
    MessageTogglePublic,
    RejectMessageView,
    RejectModerationView,
    ReSyncFromPopit,
    WriteItPopitUpdateView,
)
from nuntium.user_section.stats import StatsView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
download_attachment_view = ObjectDownloadView.as_view(model=AnswerAttachment, file_field="content")

managepatterns = patterns('',
    url(r'^$', WriteItInstanceUpdateView.as_view(), name='writeitinstance_basic_update'),
    url(r'^settings/$', WriteItInstanceAdvancedUpdateView.as_view(), name='writeitinstance_advanced_update'),
    url(r'^settings/moderation/$', WriteItInstanceModerationView.as_view(), name='writeitinstance_moderation_update'),
    url(r'^settings/maxrecipients/$', WriteItInstanceMaxRecipientsView.as_view(), name='writeitinstance_maxrecipients_update'),
    url(r'^settings/ratelimiter/$', WriteItInstanceRateLimiterView.as_view(), name='writeitinstance_ratelimiter_update'),
    url(r'^settings/answernotification/$', WriteItInstanceAnswerNotificationView.as_view(), name='writeitinstance_answernotification_update'),
    url(r'^settings/apiautoconfirm/$', WriteItInstanceApiAutoconfirmView.as_view(), name='writeitinstance_api_autoconfirm_update'),
    url(r'^settings/webbased/$', WriteItInstanceWebBasedView.as_view(), name='writeitinstance_webbased_update'),
    url(r'^settings/api/$', WriteItInstanceApiDocsView.as_view(), name='writeitinstance_api_docs'),
    url(r'^settings/sources/$', WriteitPopitRelatingView.as_view(), name='relate-writeit-popit'),
    url(r'^settings/sources/resync/(?P<popit_api_pk>[-\d]+)/$', ReSyncFromPopit.as_view(), name='resync-from-popit'),
    url(r'^settings/sources/update/(?P<pk>[-\d]+)/$', WriteItPopitUpdateView.as_view(), name='update-popit-writeit-relation'),
    url(r'^settings/templates/$', WriteItInstanceTemplateUpdateView.as_view(), name='writeitinstance_template_update'),
    url(r'^settings/templates/new_answer_notification/$', NewAnswerNotificationTemplateUpdateView.as_view(), name='edit_new_answer_notification_template'),
    url(r'^settings/templates/confirmation_template/$', ConfirmationTemplateUpdateView.as_view(), name='edit_confirmation_template'),
    url(r'^settings/templates/mailit_template/$', MailitTemplateUpdateView.as_view(), name='mailit-template-update'),
    url(r'^recipients/toggle-enabled/$',
        ToggleContactEnabledView.as_view(),
        name='toggle-enabled'),
    url(r'^recipients/$', WriteItInstanceContactDetailView.as_view(), name='contacts-per-writeitinstance'),
    url(r'^messages/$', MessagesPerWriteItInstance.as_view(), name='messages_per_writeitinstance'),
    url(r'^messages/(?P<pk>[-\d]+)/answers/$', MessageDetail.as_view(), name='message_detail_private'),
    url(r'^messages/(?P<pk>[-\d]+)/answers/create/$', AnswerCreateView.as_view(), name='create_answer'),
    url(r'^messages/(?P<message_pk>[-\d]+)/answers/(?P<pk>[-\d]+)/update/$', AnswerUpdateView.as_view(), name='update_answer'),
    url(r'^messages/(?P<pk>[-\d]+)/accept/$', AcceptMessageView.as_view(), name='accept_message'),
    url(r'^messages/(?P<pk>[-\d]+)/reject/$', RejectMessageView.as_view(), name='reject_message'),
    url(r'^stats/$', StatsView.as_view(), name='stats'),
    url(r'^pulling_status/$', WriteItInstanceStatusView.as_view(), name='pulling_status'),
    url(r'^delete/$',
        WriteItDeleteView.as_view(template_name="nuntium/profiles/writeitinstance_check_delete.html"),
        name='delete_an_instance'),
    url(r'^messages/(?P<pk>[-\d]+)/toggle-public/$', MessageTogglePublic.as_view(), name='toggle_public'),
    url(r'^moderation_accept/(?P<slug>[-\w]+)/?$', AcceptModerationView.as_view(), name='moderation_accept'),
    url(r'^moderation_reject/(?P<slug>[-\w]+)/?$', RejectModerationView.as_view(), name='moderation_rejected'),

)

write_message_wizard = WriteMessageView.as_view(url_name='write_message_step')

urlpatterns = i18n_patterns('',
    url(r'^$', WriteItInstanceDetailView.as_view(), name='instance_detail'),
    url(r'^write/sign/(?P<slug>[-\w]+)/$', ConfirmView.as_view(), name='confirm'),
    url(r'^write/sign/$', WriteSignView.as_view(), name='write_message_sign'),
    url(r'^write/(?P<step>.+)/$', write_message_wizard, name='write_message_step'),
    url(r'^write/$', write_message_wizard, name='write_message'),
    # url(r'^write/draft/$', TemplateView.as_view(template_name='write/draft.html'), name='write_draft'),
    # url(r'^write/preview/$', TemplateView.as_view(template_name='write/preview.html'), name='write_preview'),
    url(r'^threads/$', MessageThreadsView.as_view(), name='message_threads'),
    url(r'^thread/(?P<slug>[-\w]+)/$', MessageThreadView.as_view(), name='thread_read'),
    url(r'^per_person/(?P<pk>[-\d]+)/$', MessagesPerPersonView.as_view(), name='messages_per_person'),
    url(r'^from/(?P<message_slug>[-\w]+)/?$', MessagesFromPersonView.as_view(), name='all-messages-from-the-same-author-as'),
    url(r'^to/(?P<pk>[-\d]+)/$', MessagesPerPersonView.as_view(), name='thread_to'),

    url(r'^search/$', PerInstanceSearchView(), name='instance_search'),
    url(r'^attachment/(?P<pk>[-\d]+)/$', download_attachment_view, name='attachment'),
    url(r'^manage/', include(managepatterns)),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}, name='logout'),
)
