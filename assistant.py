from fuzzywuzzy import fuzz

opts = {
    "tbr": ('расскажите','скажите','покажите','сколько','произнесите','подскажите'
            ,'извините','расскажи','покажи','сколько','произнеси','скажи'),
    "cmds": {
        "theme": ('энциклопед','дом','досуг','кулинар','политик','прав','государств','детектив',
                  'учебн','обуч','литератур','мемуар',
                 'биография',),
        "mood": ('веселый','грустный','веселое','грустное','веселая','грустная'),
        "autor": ('пушкин','есенин','маяковск'),
        "name": ('гарри','поттер','1984','вишневый сад', 'дубровск'),
        "pay": ('Оплати','Оплатите','Оплатить')
        
    }
}

def recognize_cmd(request):
    RC = {'cmd': '', 'percent': 0,}
    
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(request, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
   
    return RC['cmd']

def execute_cmd(cmd):
    if cmd == 'genre':
        return cmd
   
    elif cmd == 'mood':
        return cmd
   
    elif cmd == 'author':
        return cmd
   
    else:
        return 'Команда не распознана, повторите!'
        
def requestProcess(request, opts = opts):
    request = request.lower()
    for x in opts['tbr']:
        request = request.replace(x, "").strip()
    cmd = recognize_cmd(request)
    tagIs = 0
    for tag in opts['cmds'][cmd]:
        if tag in request:
            if tagIs == 0:
                tagIs = tag
                
    if tagIs == 0:
        cmd = ''
    else:
        tagIs = tagIs.capitalize()
    return (cmd, tagIs)