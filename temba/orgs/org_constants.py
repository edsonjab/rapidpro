# coding=utf-8
################ Constants of topup table ################################
topup_style = "<style type=\'text/css\'>\n/*<![CDATA[*/\n    #id-topups.formax-summary {\n      padding-top: 0px;\n }\n\n/*]]>*/\n</style>"
topup_response_es = topup_style +"<div class = 'formax-summary'>Le quedan <span class='attn'> %s </span> créditos </br> Ha usado %s créditos desde que se registró</div>"
topup_dictionary = {'action': u'link', 'name': u'topups', 'url': u'/topup/', 'button': u'Save', 'response':'',  'icon': u'icon-coins'}

############### Constants of channel table ###############################
channel_url = '/channels/channel/read/%s'
channel_error = "<span class='errored'> última sincronización activada hace: %s </span></div>"
channel_response_es = topup_style+" <div class = 'formax_summary' style = 'padding-left: 75px; font-size:16px' ><div class='pull-right'><a class='btn btn-secondary org-button' href='/channels/channel/bulk_sender_options/?channel=%d'>     Permitir envio masivo  </a> </div>    <div class='device'>  %s <span class='number'> %s </span> </div>"#+channel_error
channel_last_sync_es = "Ultima sincronizacion  hace %s"
channel_last_sync = "Last syncronization %s"
channel_never ="Never"
channel_never_es = "Nunca"
channel_active_es = 'Activada el %s'
channel_active = 'Activated  %s'

channel_dictionary = {'action': u'link', 'name': u'channel', 'url': '', 'button': u'Save', 'response':'', 'icon': u'icon-channel-android'}


def to_human_date_es (date):
    return "%d de %d del %d a las %d:%d" % (date.day, date.month, date.year, (date.hour-5)%24, date.minute)
