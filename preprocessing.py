import pandas as pd
# import LSA
from time import time
import re
from pymorphy2 import MorphAnalyzer

def read_dataframe(filename, names):
    return pd.read_csv(filename, sep='\t', names=names,
                    encoding='cp1251', error_bad_lines=False)



def pre_processing(dataset):
    pd.options.mode.chained_assignment = None
    tic = time()
    for i in range(len(dataset)):
        dataset[i] = dataset[i].lower()
        dataset[i] = re.sub(r'<[^>]+>', ' ', dataset[i])
        dataset[i] = dataset[i].replace(u'- ', '  ')
        dataset[i] = dataset[i].replace(u'.', '  ')
        dataset[i] = dataset[i].replace(u'№', '  ')
        dataset[i] = dataset[i].replace(u',', '  ')
        dataset[i] = dataset[i].replace(u'(', '  ')
        dataset[i] = dataset[i].replace(u')', '  ')
        dataset[i] = dataset[i].replace(u':', '  ')
        dataset[i] = dataset[i].replace(u'&#', '  ')
        dataset[i] = dataset[i].replace(u';', '  ')
        dataset[i] = dataset[i].replace(u'|', '  ')
        dataset[i] = re.sub(r' +', ' ', dataset[i])


        dataset[i] = dataset[i].replace(u' дч', '  ')

        dataset[i] = dataset[i].replace(u' б ', '  ')
        dataset[i] = dataset[i].replace(u' в ', '  ')
        dataset[i] = dataset[i].replace(u' г ', '  ')
        dataset[i] = dataset[i].replace(r' г ', '  ')
        dataset[i] = dataset[i].replace(u' д ', '  ')
        dataset[i] = dataset[i].replace(u' е ', '  ')
        dataset[i] = dataset[i].replace(u' ж ', '  ')
        dataset[i] = dataset[i].replace(u' э ', '  ')
        dataset[i] = dataset[i].replace(u' и ', '  ')
        dataset[i] = dataset[i].replace(u' к ', '  ')
        dataset[i] = dataset[i].replace(u' л ', '  ')
        dataset[i] = dataset[i].replace(u' м ', '  ')
        dataset[i] = dataset[i].replace(u' н ', '  ')
        dataset[i] = dataset[i].replace(u' о ', '  ')
        dataset[i] = dataset[i].replace(u' п ', '  ')
        dataset[i] = dataset[i].replace(u' р ', '  ')
        dataset[i] = dataset[i].replace(u' с ', '  ')
        dataset[i] = dataset[i].replace(r' с ', '  ')
        dataset[i] = dataset[i].replace(u' т ', '  ')
        dataset[i] = dataset[i].replace(u' у ', '  ')
        dataset[i] = dataset[i].replace(u' ф ', '  ')
        dataset[i] = dataset[i].replace(u' х ', '  ')
        dataset[i] = dataset[i].replace(u' ц ', '  ')
        dataset[i] = dataset[i].replace(u' ч ', '  ')
        dataset[i] = dataset[i].replace(u' ш ', '  ')
        dataset[i] = dataset[i].replace(u' щ ', '  ')
        dataset[i] = dataset[i].replace(u' й ', '  ')
        dataset[i] = dataset[i].replace(u' э ', '  ')
        dataset[i] = dataset[i].replace(u' ю ', '  ')
        dataset[i] = dataset[i].replace(u' я ', '  ')
        dataset[i] = dataset[i].replace(u' ы ', '  ')
        dataset[i] = dataset[i].replace(u' ь ', '  ')
        dataset[i] = dataset[i].replace(u' ъ ', '  ')




        dataset[i] = dataset[i].replace(u' берем ', u'беременность ')
        dataset[i] = dataset[i].replace(u' наследственность не отягощена', u'наследственность_не_отягощена ')

        dataset[i] = dataset[i].replace(u'гркл', u'грудной клетке ')
        dataset[i] = dataset[i].replace(u' стен([а-я]*)(-)([0-9]*)(\.)?', u' стенокардия  ')
        dataset[i] = dataset[i].replace(u' напряж([а-я]*)(-)([0-9]*)(\.)?', u' напряжения  ')
        dataset[i] = dataset[i].replace(u' нест([а-я]*)(-)([0-9]*)(\.)?', u' нестабильная  ')
        dataset[i] = dataset[i].replace(u' прогрес([а-я]*)(-)([0-9]*)(\.)?', u' прогрессирующая  ')
        dataset[i] = dataset[i].replace(u' гиперто([а-я]*)(-)([0-9]*)(\.)?', u' гипертоническа я ')
        dataset[i] = dataset[i].replace(u' желудочко([а-я]*)(-)([0-9]*)(\.)?', u' желудочновая  ')
        dataset[i] = dataset[i].replace(u' нестабиль([а-я]*)(-)([0-9]*)(\.)?', u' нестабильная  ')
        # dataset[i] = dataset[i].replace(u' от', u' от  ')
        dataset[i] = dataset[i].replace(u' значемы([а-я]*)(-)([0-9]*)(\.)?', u' значимые  ')
        dataset[i] = dataset[i].replace(u' идиопа([а-я]*)(-)([0-9]*)(\.)?', u' идиопатические  ')
        dataset[i] = dataset[i].replace(u' коронарн([а-я]*)(-)([0-9]*)(\.)?', u' коронарных  ')
        dataset[i] = dataset[i].replace(u' неуточненн([а-я]*)(-)([0-9]*)(\.)?', u' неуточненная  ')
        dataset[i] = dataset[i].replace(u' оим', u' острый инфаркт миокарда  ')
        dataset[i] = dataset[i].replace(u'оим ', u'острый инфаркт миокарда  ')
        dataset[i] = dataset[i].replace(u' постинфарктный', u' постинфарктный  ')
        dataset[i] = dataset[i].replace(u' постинф([а-я]*)(-)([0-9]*)(\.)?', u' постинфарктный ')
        # dataset[i] = dataset[i].replace(u' стенокардия напряжения', u' стенокардия_напряжения ')
        # dataset[i] = dataset[i].replace(u' нестабильная стенокардия', u' нестабильная_стенокардия ')
        # dataset[i] = dataset[i].replace(u'ибс', u'ибс  ')
        dataset[i] = dataset[i].replace(u' сн ', u' сердечная недостаточность  ')
        dataset[i] = dataset[i].replace(u' прогр ', u' прогрессирующий  ')
        dataset[i] = dataset[i].replace(u' фк', u' функциональный_класс ')
        dataset[i] = dataset[i].replace(u'фк ', u' функциональный_класс  ')
        dataset[i] = dataset[i].replace(u'фк', u' функциональный_класс  ')
        dataset[i] = dataset[i].replace(u'ф к', u' функциональный_класс  ')
        dataset[i] = dataset[i].replace(u' прогре([а-я]*)(-)([0-9]*)(\.)?', u' прогрессирующий ')
        dataset[i] = dataset[i].replace(u' стентиров([а-я]*)(-)([0-9]*)(\.)?', u' стентирование ')
        dataset[i] = dataset[i].replace(u' шутн([а-я]*)(-)([0-9]*)(\.)?', u' шунтирование ')

        # dataset[i] = dataset[i].replace(u' сн ', u' сердечная_недостаточность ')
        dataset[i] = dataset[i].replace(u' недостаточность', u' недостаточность  ')
        dataset[i] = dataset[i].replace(u' напряжения', u' напражения  ')
        dataset[i] = dataset[i].replace(u' нестабильная ', u' нестабильная  ')
        dataset[i] = dataset[i].replace(u' нестабил([а-я]*)(-)([0-9]*)(\.)?', u' нестабильная ')
        # dataset[i] = dataset[i].replace(u' гб', u' гипертоническая_болезнь ')
        # dataset[i] = dataset[i].replace(u'гб ', u'гипертоническая_болезнь  ')
        dataset[i] = dataset[i].replace(u' им ', u' инфаркт_миокарда  ')
        # dataset[i] = dataset[i].replace(u'\(им', u'(инфаркт миокарда  ')
        dataset[i] = dataset[i].replace(u' нест ', u' нестабильная  ')
        dataset[i] = dataset[i].replace(u'нестаб ', u'нестабильная  ')
        dataset[i] = dataset[i].replace(u'инф ', u'инфаркт  ')
        # dataset[i] = dataset[i].replace(u' им ', u' инфаркт_миокарда  ')
        dataset[i] = dataset[i].replace(u' кардиосклероз', u'кардиосклероз  ')
        dataset[i] = dataset[i].replace(u' болезнь', u' болезнь  ')
        dataset[i] = dataset[i].replace(u' нестаб ', u' нестабильная  ')
        dataset[i] = dataset[i].replace(u' им ', u' инфаркт_миокарда  ')
        dataset[i] = dataset[i].replace(u' нестабильнаястенокардия', u' нестабильная_стенокардия ')
        dataset[i] = dataset[i].replace(u' лж', u' левого желудочка ')
        dataset[i] = dataset[i].replace(u'акш ', u' аортокоронарное шунтирование  ')
        dataset[i] = dataset[i].replace(u' ссо', u' сердечно_сосудистых_осложнений  ')
        dataset[i] = dataset[i].replace(u' прогр ', u' прогрессирующая  ')
        dataset[i] = dataset[i].replace(u'нест ', u'нестабильная  ')
        dataset[i] = dataset[i].replace(u' нест ', u' нестабильная  ')
        dataset[i] = dataset[i].replace(u' напряж ', u' напряжения  ')
        dataset[i] = dataset[i].replace(u'прогресс ', u'прогрессирующая  ')
        dataset[i] = dataset[i].replace(u' прогресс ', u' прогрессирующая  ')
        dataset[i] = dataset[i].replace(u' риск', u' риск  ')

        dataset[i] = dataset[i].replace(u'ас-з', u' атеросклероз  ')
        dataset[i] = dataset[i].replace(u'(\s+)', '  ')
        dataset[i] = dataset[i].replace(u' iii', u' 3 ')
        dataset[i] = dataset[i].replace(u' ii', u' 2 ')
        dataset[i] = dataset[i].replace(u' i', u' 1 ')

        dataset[i] = dataset[i].replace(u'iii ', u'3  ')
        dataset[i] = dataset[i].replace(u'ii ', u'2  ')
        dataset[i] = dataset[i].replace(u'i ', u'1  ')
        dataset[i] = dataset[i].replace(u' риск 4', u' риск_4 ')
        dataset[i] = dataset[i].replace(u' риск 3', u' риск_3 ')
        dataset[i] = dataset[i].replace(u' риск 2', u' риск_2 ')
        dataset[i] = dataset[i].replace(u' риск 1', u' риск_1 ')
        dataset[i] = dataset[i].replace(u'ст ', u' стадия  ')
        dataset[i] = dataset[i].replace(u' ст ', u' стадия  ')
        dataset[i] = dataset[i].replace(u'(\s+)', '  ')

        dataset[i] = dataset[i].replace(u'3 стадия ', u'3_стадия  ')
        dataset[i] = dataset[i].replace(u'2 стадия ', u'2_стадия  ')
        dataset[i] = dataset[i].replace(u'1 стадия ', u'1_стадия  ')
        dataset[i] = dataset[i].replace(u'ф кл', u' функциональный_класс ')
        dataset[i] = dataset[i].replace(u'(\s+)', '  ')

        dataset[i] = dataset[i].replace(u' нс ', u' нестабильная_стенокардия  ')
        dataset[i] = dataset[i].replace(u'ибчс', ' ибс  ')
        dataset[i] = dataset[i].replace(u'исб', ' ибс  ')
        dataset[i] = dataset[i].replace(u'ибс ', u'ишемическая_болезнь_сердца  ')
        dataset[i] = dataset[i].replace(u'ибс:', u'ишемическая_болезнь_сердца ')
        dataset[i] = dataset[i].replace(u'ибс', u'ишемическая_болезнь_сердца  ')
        dataset[i] = dataset[i].replace(u'сд ', u' сахарный_диабет  ')
        dataset[i] = dataset[i].replace(u' стентиров ', u' стентирование  ')
        dataset[i] = dataset[i].replace(u' нс', u' нестабильная_стенокардия  ')
        dataset[i] = dataset[i].replace(u' хсн', u' хроническая_сердечная_недостаточность  ')
        dataset[i] = dataset[i].replace(u'жел ', u'желудочковая  ')
        dataset[i] = dataset[i].replace(u' экстр ', u' экстрасистолия  ')
        dataset[i] = dataset[i].replace(u' желл ', u' желудочковая   ')
        dataset[i] = dataset[i].replace(u' ст-я', u' стадия   ')

        dataset[i] = dataset[i].replace(u' оим ', u'острый_инфаркт_миокарда  ')
        dataset[i] = dataset[i].replace(u' окс ', u'острый_коронарный_синдром  ')
        dataset[i] = dataset[i].replace(u'код по мкб10 ', '  ')
        dataset[i] = dataset[i].replace(u' р3 ', ' риск_3  ')
        # dataset[i] = dataset[i].replace(u'гб', 'гипертоническая_болезнь  ')
        dataset[i] = dataset[i].replace(u' р4 ', ' риск_4  ')
        dataset[i] = dataset[i].replace(u' р2 ', ' риск_2  ')
        dataset[i] = dataset[i].replace(u' р1 ', ' риск_1  ')
        dataset[i] = dataset[i].replace(u'(\s+)', '  ')
        dataset[i] = dataset[i].replace(u'бца', 'брахиоцефальных артерий ')
        dataset[i] = dataset[i].replace(u'гипертоническая болезнь 3 ', 'гипертоническая_болезнь 3_степень  ')
        dataset[i] = dataset[i].replace(u'гипертоническая болезнь 2 ', 'гипертоническая_болезнь 2_степень  ')
        dataset[i] = dataset[i].replace(u'гипертоническая болезнь 1', 'гипертоническая_болезнь 1_степень  ')
        dataset[i] = dataset[i].replace(u'гипертоническая болезнь 3_стадия', 'гипертоническая_болезнь 3_степень  ')
        dataset[i] = dataset[i].replace(u'гипертоническая болезнь 2_стадия', 'гипертоническая_болезнь 3_степень  ')
        dataset[i] = dataset[i].replace(u'гипертоническая болезнь 1_стадия', 'гипертоническая_болезнь 3_степень  ')
        dataset[i] = dataset[i].replace(u'напр-я', 'напряжения  ')
        dataset[i] = dataset[i].replace(u'напряжен([а-я]*)(-)([0-9]*)(\.)?', u' напряжения  ')
        dataset[i] = dataset[i].replace(u'(\s+)', '  ')
        dataset[i] = dataset[i].replace(u'пфп', 'пароксизмальная_фибрилляция_предсердий ')
        dataset[i] = dataset[i].replace(u'пфп', 'пароксизмальная_фибрилляция_предсердий ')
        dataset[i] = dataset[i].replace(u'хр ', 'хронический  ')

        dataset[i] = dataset[i].replace(u' 11г', ' 11 ')
        dataset[i] = dataset[i].replace(u'11г', '11 ')
        dataset[i] = dataset[i].replace(u' 2011г', ' 2011 ')
        dataset[i] = dataset[i].replace(u'2011г', '2011 ')
        dataset[i] = dataset[i].replace(u'2011 г', '2011 ')

        dataset[i] = dataset[i].replace(u' 12г', ' 12 ')
        dataset[i] = dataset[i].replace(u'12г', '12 ')
        dataset[i] = dataset[i].replace(u' 2012г', ' 2012 ')
        dataset[i] = dataset[i].replace(u'2012г', '2012 ')
        dataset[i] = dataset[i].replace(u'2012 г', '2012 ')

        dataset[i] = dataset[i].replace(u' 13г', ' 13 ')
        dataset[i] = dataset[i].replace(u'13г', '13 ')
        dataset[i] = dataset[i].replace(u' 2013г', ' 2013 ')
        dataset[i] = dataset[i].replace(u'2013г', '2013 ')
        dataset[i] = dataset[i].replace(u'2013 г', '2013 ')

        dataset[i] = dataset[i].replace(u' 12072013?', ' 12072013 ')

        dataset[i] = dataset[i].replace(u' 14г', ' 14 ')
        dataset[i] = dataset[i].replace(u'14г', '14 ')
        dataset[i] = dataset[i].replace(u' 2014г', ' 2014 ')
        dataset[i] = dataset[i].replace(u'2014г', '2014 ')
        dataset[i] = dataset[i].replace(u'2014 г', '2014 ')

        dataset[i] = dataset[i].replace(u' 15г', ' 15 ')
        dataset[i] = dataset[i].replace(u'15г', '15 ')
        dataset[i] = dataset[i].replace(u' 2015г', ' 2015 ')
        dataset[i] = dataset[i].replace(u'2015г', '2015 ')
        dataset[i] = dataset[i].replace(u'2015 г', '2015 ')

        dataset[i] = dataset[i].replace(u' 16г', ' 16 ')
        dataset[i] = dataset[i].replace(u'16г', '16 ')
        dataset[i] = dataset[i].replace(u' 2016г', ' 2016 ')
        dataset[i] = dataset[i].replace(u'2016г', '2016 ')
        dataset[i] = dataset[i].replace(u'2016 г', '2016 ')

        dataset[i] = dataset[i].replace(u' 2009г', ' 2009 ')
        dataset[i] = dataset[i].replace(u' 2007г', ' 2007 ')
        dataset[i] = dataset[i].replace(u' 2006г', ' 2006 ')
        dataset[i] = dataset[i].replace(u' 2005г', ' 2005 ')
        dataset[i] = dataset[i].replace(u' 2004г', ' 2004 ')
        dataset[i] = dataset[i].replace(u' 2010г', ' 2010 ')
        dataset[i] = dataset[i].replace(u' 2002г', ' 2002 ')
        dataset[i] = dataset[i].replace(u' 2001г', ' 2001 ')
        dataset[i] = dataset[i].replace(u' 1999г', ' 1999 ')
        dataset[i] = dataset[i].replace(u' 1997г', ' 1997 ')
        dataset[i] = dataset[i].replace(u' 1994г', ' 1994 ')
        dataset[i] = dataset[i].replace(u' 1992г', ' 1992 ')
        dataset[i] = dataset[i].replace(u' 09г', ' 09 ')
        dataset[i] = dataset[i].replace(u' 2000гг', ' 2000 ')
        dataset[i] = dataset[i].replace(u' 2000гг', ' 2000 ')
        dataset[i] = dataset[i].replace(u' 2г', ' 2002 ')
        dataset[i] = dataset[i].replace(u' 2015ю', ' 2015 ')
        dataset[i] = dataset[i].replace(u' 1984г', ' 1984 ')
        dataset[i] = dataset[i].replace(u' миокардаот', ' миокарда от  ')

        dataset[i] = dataset[i].replace(u' ccо-4', ' сердечно_сосудистых_осложнений_4  ')
        dataset[i] = dataset[i].replace(u' чка', ' ангиопластика_коронарных_артерий  ')
        dataset[i] = dataset[i].replace(u' чкв', ' ангиопластика_коронарных_артерий  ')
        dataset[i] = dataset[i].replace(u' чтка', ' ангиопластика_коронарных_артерий  ')
        dataset[i] = dataset[i].replace(u' ptca', ' ангиопластика_коронарных_артерий  ')
        dataset[i] = dataset[i].replace(u' rca', ' правая коронарная артерия  ')
        # dataset[i] = dataset[i].replace(u'ав', ' атриовентрикулярный  ')
        dataset[i] = dataset[i].replace(u' аг ', ' гипертоническая_болезнь  ')
        dataset[i] = dataset[i].replace(u' ак-з', ' атеросклеротический_кардиосклероз  ')
        dataset[i] = dataset[i].replace(u' актг-синдром', ' адренокортикотропный гормон  ')
        dataset[i] = dataset[i].replace(u' актг', ' адренокортикотропный гормон  ')
        dataset[i] = dataset[i].replace(u' аок', ' аортальный клапан  ')
        dataset[i] = dataset[i].replace(u' ас+ан', ' аортальный стеноз в сочетании с аортальной недостаточностью  ')
        dataset[i] = dataset[i].replace(u' аскс', ' атеросклеротический_кардиосклероз  ')
        dataset[i] = dataset[i].replace(u' басс', ' бассейн  ')
        dataset[i] = dataset[i].replace(u' бца', ' брахиоцефальные артерии  ')
        dataset[i] = dataset[i].replace(u' вабк', ' внутриаортальная баллонная контрпульсация  ')
        dataset[i] = dataset[i].replace(u' вбб', ' вертебробазиллярный бассейн  ')
        # dataset[i] = dataset[i].replace(u'воз', ' Всемирная Организация Здравоохранения  ')
        dataset[i] = dataset[i].replace(u' впс', ' врождённый_порок_сердца  ')
        dataset[i] = dataset[i].replace(u' вса', ' внутренняя сонная артерия  ')
        dataset[i] = dataset[i].replace(u' втпж', ' выносящий тракт правого желудочка  ')
        dataset[i] = dataset[i].replace(u' втлж', ' выносящий тракт левого желудочка  ')
        dataset[i] = dataset[i].replace(u' глж', ' гипертрофия_левого_желудочка  ')
        dataset[i] = dataset[i].replace(u' дмжп', ' дефект межжелудочковой перегородки  ')
        dataset[i] = dataset[i].replace(u' дуз', ' диффузный узловой зоб  ')
        dataset[i] = dataset[i].replace(u' збв', ' задне-боковая ветвь  ')
        dataset[i] = dataset[i].replace(u' змкт', ' мультиспиральная компьютерная томография  ')
        dataset[i] = dataset[i].replace(u' зно', ' злокачественное_новообразование  ')
        dataset[i] = dataset[i].replace(u' зслж', ' задняя стенка левого желудочка  ')
        # dataset[i] = dataset[i].replace(u'ибчс', ' ибс  ')
        dataset[i] = dataset[i].replace(u' икд', ' имплантируемый кардиовертер-дефибриллятор  ')
        dataset[i] = dataset[i].replace(u' илв', ' изоляция лёгочных вен  ')
        dataset[i] = dataset[i].replace(u' инрс', ' нарушения_ритма_сердца  ')
        # dataset[i] = dataset[i].replace(u'исб', ' ибс  ')
        dataset[i] = dataset[i].replace(u' каг', ' коронарная_ангиография  ')
        dataset[i] = dataset[i].replace(u' ккп', ' кровяная_кардиоплегия  ')
        dataset[i] = dataset[i].replace(u' лвга', ' левая внутренняя грудная артерия  ')
        dataset[i] = dataset[i].replace(u' лг2', ' лёгочная_гипертензия 2_стадия  ')
        dataset[i] = dataset[i].replace(u' лп', ' левое предсердие  ')
        dataset[i] = dataset[i].replace(u' мв-оа', ' маргинальная ветвь огибающей артерии  ')
        dataset[i] = dataset[i].replace(u' мк', ' митральный клапан  ')
        dataset[i] = dataset[i].replace(u' мкш', ' маммаро-коронарное_шунтирование  ')
        # dataset[i] = dataset[i].replace(u'мн', ' митральная_недостаточность  ')
        dataset[i] = dataset[i].replace(u' напр ', ' направление  ')
        dataset[i] = dataset[i].replace(u' нрс', ' нарушения_ритма_сердца  ')
        dataset[i] = dataset[i].replace(u' оа', ' огибающая артерия  ')
        dataset[i] = dataset[i].replace(u' оаанк', ' облитерирующий_атеросклероз_артерий_нижних_конечностей  ')
        dataset[i] = dataset[i].replace(u' оаснк', ' облитерирующий_атеросклероз_сосудов_нижних_конечностей  ')
        dataset[i] = dataset[i].replace(u' оим', ' острый_инфаркт_миокарда  ')
        dataset[i] = dataset[i].replace(u' окн', ' острая_коронарная_недостаточность  ')
        dataset[i] = dataset[i].replace(u' оксот', ' острый_коронарный_синдром от  ')
        dataset[i] = dataset[i].replace(u' олжн', ' острая_левожелудочковая_недостаточность  ')
        dataset[i] = dataset[i].replace(u' омс', ' обязательное медицинское страхование  ')
        dataset[i] = dataset[i].replace(u' онмк', ' острое_нарушение_мозгового_кровообращения  ')
        dataset[i] = dataset[i].replace(u' осл ', ' осложнение  ')
        dataset[i] = dataset[i].replace(u' пблнпг', ' полная_блокада_левой_ножки_пучка_гиса  ')
        dataset[i] = dataset[i].replace(u' пввлнпг', ' передне-верхняя ветвь левой ножки пучка гиса  ')
        dataset[i] = dataset[i].replace(u' пж', ' правый желудочек  ')
        dataset[i] = dataset[i].replace(u' пикс', ' постинфарктный_кардиосклероз  ')
        dataset[i] = dataset[i].replace(u' пка', ' правая коронарная артерия  ')
        dataset[i] = dataset[i].replace(u' пмжа', ' передняя межжелудочковая артерия  ')
        dataset[i] = dataset[i].replace(u' пнпг', ' правая ножка пучка гиса  ')
        dataset[i] = dataset[i].replace(u' повт ', ' повторный  ')
        dataset[i] = dataset[i].replace(u' птффп', ' пароксизм_трепетения_фибрилляции_предсердий  ')
        dataset[i] = dataset[i].replace(u' пффп', ' пфп  ')
        dataset[i] = dataset[i].replace(u' пфп', ' пароксизм_фибрилляции_предсердий  ')
        dataset[i] = dataset[i].replace(u' пфр', ' пенсионный фонд РФ  ')
        dataset[i] = dataset[i].replace(u' рвв', ' ретровентрикулярная ветвь  ')
        dataset[i] = dataset[i].replace(u' рец', ' рецидив  ')
        dataset[i] = dataset[i].replace(u' рсла', ' ptca  ')
        dataset[i] = dataset[i].replace(u' ртса', ' ptca  ')
        dataset[i] = dataset[i].replace(u' рчи', ' радиочастотная_изоляция  ')
        dataset[i] = dataset[i].replace(u' рсла', ' ptca  ')
        dataset[i] = dataset[i].replace(u' соп', ' сопутствующий диагноз  ')
        dataset[i] = dataset[i].replace(u' сссу', ' синдром_слабости_синусового_узла  ')
        dataset[i] = dataset[i].replace(u' стл', ' системный тромболизис  ')
        dataset[i] = dataset[i].replace(u' стлт', ' системная тромболитическая терапия  ')
        dataset[i] = dataset[i].replace(u' тбка', ' ptca  ')
        dataset[i] = dataset[i].replace(u' тиа', ' транзиторная_ишемическая_атака  ')
        dataset[i] = dataset[i].replace(u' тлбап', ' ptca транслюминальная балонная ангиопластика  ')
        dataset[i] = dataset[i].replace(u' тлт', ' тромболитическая терапия  ')
        dataset[i] = dataset[i].replace(u' тур ', ' трансуретральная резекция  ')
        dataset[i] = dataset[i].replace(u' тэ ', ' тромбоэмболия  ')
        dataset[i] = dataset[i].replace(u' тэмвла ', ' тромбоэмболия_мелких_ветвей_лёгочной_артерии  ')
        dataset[i] = dataset[i].replace(u' фг1', ' фиброгастроскопия  ')
        dataset[i] = dataset[i].replace(u' фтп', ' фибрилляция-трепетание предсердий  ')
        dataset[i] = dataset[i].replace(u' хрбс', ' хроническая_ревматическая_болезнь_сердца  ')
        dataset[i] = dataset[i].replace(u' хсн', ' хроническая_сердечная_недостаточность  ')
        dataset[i] = dataset[i].replace(u' чрбс', ' искажённая_хроническая_ревматическая_болезнь_сердца  ')
        dataset[i] = dataset[i].replace(u' экс', ' электрокардиостимулятор  ')
        dataset[i] = dataset[i].replace(u' эктоп', ' эктопический  ')
        dataset[i] = dataset[i].replace(u' гкмп ', 'гипертрофическая_кардиомиопатия  ')
        dataset[i] = dataset[i].replace(u' острый инфаркт миокарда', ' острый_инфаркт_миокарда  ')

        dataset[i] = dataset[i].replace(u'[0-9]', ' ')

        dataset[i] = dataset[i].replace(u' г$', ' ')
        dataset[i] = dataset[i].replace(u'(\s+)', '  ')

        # жалобы

        # вырезаем ненужные слова

        dataset[i] = dataset[i].replace(u' пациент ', '  ')
        dataset[i] = dataset[i].replace(u' пациент ', '  ')
        dataset[i] = dataset[i].replace(u'пациент ', ' ')
        dataset[i] = dataset[i].replace(u'на момент осмотра ', '  ')
        dataset[i] = dataset[i].replace(u'при поступлении', ' ')
        dataset[i] = dataset[i].replace(u'с и/б и анамнезом ознакомлены', ' ')
        dataset[i] = dataset[i].replace(u'причина обращения', ' ')
        dataset[i] = dataset[i].replace(u'з/о', ' ')
        dataset[i] = dataset[i].replace(u'дата', ' ')
        dataset[i] = dataset[i].replace(u'больного в отделении кардиологии приняли', ' ')

        dataset[i] = dataset[i].replace(u'больного в отделении кардиологии приняли вр', ' ')
        dataset[i] = dataset[i].replace(u'морошкина н.в.', ' ')
        dataset[i] = dataset[i].replace(u'соловьёва н.в.', ' ')
        dataset[i] = dataset[i].replace(u'совместный осмотр заведующего отделением', ' ')
        dataset[i] = dataset[i].replace(u'осмотр дежурным реаниматологом', ' ')
        dataset[i] = dataset[i].replace(u'больную в отделении кардиологии приняли', ' ')
        dataset[i] = dataset[i].replace(u'больную в отделении кардиолоubb приняли', ' ')
        dataset[i] = dataset[i].replace(u'вр ,', ' ')
        dataset[i] = dataset[i].replace(u'вр,', ' ')
        # dataset[i] = dataset[i].replace(u'вр.', ' ')

        dataset[i] = dataset[i].replace(u'больную в отделении кардиологии приняла', ' ')
        dataset[i] = dataset[i].replace(u'при посуплении', ' ')

        dataset[i] = dataset[i].replace(u' предъявляет жалобы на ', '  ')
        dataset[i] = dataset[i].replace(u'предъявляет жалобы на ', ' ')
        dataset[i] = dataset[i].replace(u' жалобы на ', '  ')
        dataset[i] = dataset[i].replace(u'жалобы на ', ' ')
        dataset[i] = dataset[i].replace(u' эпизод ', '  ')
        dataset[i] = dataset[i].replace(u'эпизод ', ' ')
        dataset[i] = dataset[i].replace(u'эпизоды ', ' ')
        dataset[i] = dataset[i].replace(u' эпизоды ', '  ')
        dataset[i] = dataset[i].replace(u' эпизодом ', '  ')
        dataset[i] = dataset[i].replace(u' обл ', ' области  ')
        dataset[i] = dataset[i].replace(u'повышение т тела', 'повышение_температуры_тела ')
        dataset[i] = dataset[i].replace(u'повышением температуры', 'повышение_температуры_тела ')
        dataset[i] = dataset[i].replace(u'повышение температуры тела', 'повышение_температуры_тела ')

        dataset[i] = dataset[i].replace(u'с и/б', ' ')
        dataset[i] = dataset[i].replace(u'доставлен бригадой с/п', ' ')
        dataset[i] = dataset[i].replace(u'с дежурным реаниматологом', ' ')

        dataset[i] = dataset[i].replace(u'жалоб не предъявляет', 'жалоб_не_предъявляет ')
        # dataset[i] = dataset[i].replace(u'. жалоб_не_предъявляет. . жалоб_не_предъявляет.', 'жалоб_не_предъявляет ')
        dataset[i] = dataset[i].replace(u'плановая консультация', 'жалоб_не_предъявляет ')
        dataset[i] = dataset[i].replace(u'одышка в покое и при расширении двигательного режима отрицает',
                                                'одышку_отрицает  ')

        # dataset[i] = dataset[i].replace(u'.. мя', ' ')
        dataset[i] = dataset[i].replace(u'время ', '  ')
        dataset[i] = dataset[i].replace(u' пархоменко', '  ')
        dataset[i] = dataset[i].replace(u'зуева и.б.', ' ')
        dataset[i] = dataset[i].replace(u'при осмотре', ' ')
        dataset[i] = dataset[i].replace(u'/', '  ')
        # dataset[i] = dataset[i].replace(u'.. осмотр ', ' ')
        dataset[i] = dataset[i].replace(u'осмотр зав отд ко', ' ')
        dataset[i] = dataset[i].replace(u'леч врача', ' ')
        dataset[i] = dataset[i].replace(u'смирновой', ' ')
        dataset[i] = dataset[i].replace(u'иногда отмечает', ' ')
        dataset[i] = dataset[i].replace(u'совместный осмотр', ' ')
        dataset[i] = dataset[i].replace(u'активно ', '  ')
        dataset[i] = dataset[i].replace(u'сегодня ', '  ')
        dataset[i] = dataset[i].replace(u'анамнезом ознакомлены', ' ')
        dataset[i] = dataset[i].replace(u'ощущения ', ' ')
        dataset[i] = dataset[i].replace(u'ноющего характера', 'ноющая ')
        dataset[i] = dataset[i].replace(u'для осмотра в связи с', ' ')
        dataset[i] = dataset[i].replace(u'результатам обследования от', ' ')
        dataset[i] = dataset[i].replace(u'на этаж', ' ')
        dataset[i] = dataset[i].replace(u'малейшей', ' ')
        dataset[i] = dataset[i].replace(u'со слов', '  ')
        dataset[i] = dataset[i].replace(u'различного характера', ' ')
        dataset[i] = dataset[i].replace(u' нарастание ', '  ')
        dataset[i] = dataset[i].replace(u' субъективно ', '  ')
        dataset[i] = dataset[i].replace(u' симптомокомплекс ', '  ')
        dataset[i] = dataset[i].replace(u' цифр ', '  ')
        dataset[i] = dataset[i].replace(u' ощущение', '  ')
        dataset[i] = dataset[i].replace(u' редкий', '  ')
        dataset[i] = dataset[i].replace(u'пациента в кардиологическом отделении приняли', ' ')
        dataset[i] = dataset[i].replace(u'ощущает ', '  ')
        dataset[i] = dataset[i].replace(u'лапушкиным_с_н ', '  ')
        dataset[i] = dataset[i].replace(u'при посступлении', '  ')
        dataset[i] = dataset[i].replace(u'в отделение', '  ')
        dataset[i] = dataset[i].replace(u'в отделении ', '  ')
        dataset[i] = dataset[i].replace(u'субъективно ', '  ')
        dataset[i] = dataset[i].replace(u'больного приняли', ' ')
        dataset[i] = dataset[i].replace(u'совсместно', ' ')
        dataset[i] = dataset[i].replace(u'сбор жалоб и анамнеза затруднен', ' ')
        dataset[i] = dataset[i].replace(u' возникающую ', '  ')
        dataset[i] = dataset[i].replace(u' верхушки ', '  ')
        dataset[i] = dataset[i].replace(u'с зозуевой иб', ' ')
        dataset[i] = dataset[i].replace(u'преимущественно', ' ')
        dataset[i] = dataset[i].replace(u'__волошиновой_ап', ' ')
        dataset[i] = dataset[i].replace(u'врморошкина нв', ' ')
        dataset[i] = dataset[i].replace(u'соловьёва нв', ' ')
        dataset[i] = dataset[i].replace(u'периодически', ' ')
        dataset[i] = dataset[i].replace(u'для осмотра перед плановым кхл', ' ')
        dataset[i] = dataset[i].replace(u' явился ', ' ')
        dataset[i] = dataset[i].replace(u' направлен ', ' ')
        dataset[i] = dataset[i].replace(u'лапушкина сн ', ' ')
        dataset[i] = dataset[i].replace(u'воробьёва ав ', ' ')
        dataset[i] = dataset[i].replace(u'парестезии ', '  ')
        dataset[i] = dataset[i].replace(u'резкое ', '  ')
        dataset[i] = dataset[i].replace(u'на отделении', ' ')
        dataset[i] = dataset[i].replace(u'ананезом ознакомлены', ' ')
        dataset[i] = dataset[i].replace(u'доплоннений нет', ' ')
        dataset[i] = dataset[i].replace(u'кардилогии ', '  ')
        dataset[i] = dataset[i].replace(u'приняля ', '  ')
        dataset[i] = dataset[i].replace(u'контакт с пациентом крайне затруднен', '  ')
        dataset[i] = dataset[i].replace(u'контакт с пациентом затруднен', '  ')
        dataset[i] = dataset[i].replace(u'совместно с и о зав', '  ')
        dataset[i] = dataset[i].replace(u'совместно с и о зав', '  ')
        dataset[i] = dataset[i].replace(u'галенко вл', '  ')
        dataset[i] = dataset[i].replace(u'постоянный ', '  ')
        dataset[i] = dataset[i].replace(u'интенсивные ', '  ')
        dataset[i] = dataset[i].replace(u'незначительные ', '  ')
        dataset[i] = dataset[i].replace(u' возникает ', '  ')
        dataset[i] = dataset[i].replace(u' умеренную', '  ')
        dataset[i] = dataset[i].replace(u'поступает по скорой помощи', '  ')
        dataset[i] = dataset[i].replace(u'припоступлении', '  ')
        dataset[i] = dataset[i].replace(u'отдленеии ', '  ')
        dataset[i] = dataset[i].replace(u'дополнений нет', '  ')
        dataset[i] = dataset[i].replace(u'за прошедшие сутки', ' ')
        dataset[i] = dataset[i].replace(u'переведен из гб', ' ')
        dataset[i] = dataset[i].replace(u'эпизодов ', '  ')
        dataset[i] = dataset[i].replace(u'переведен из', ' ')
        dataset[i] = dataset[i].replace(u'бригадой с пом', ' ')
        dataset[i] = dataset[i].replace(u'анамнезом озанкомлены', ' ')
        dataset[i] = dataset[i].replace(u'ускоренным шагом ', ' ')
        dataset[i] = dataset[i].replace(u'- ', '  ')
        dataset[i] = dataset[i].replace(u'соловьёвой н в н а', '  ')
        dataset[i] = dataset[i].replace(u' бригадой сп', '  ')
        dataset[i] = dataset[i].replace(u' перенес', '  ')
        dataset[i] = dataset[i].replace(u' перенесла', '  ')
        dataset[i] = dataset[i].replace(u' транспортировку', '  ')
        dataset[i] = dataset[i].replace(u'самостоятельно ', '  ')
        dataset[i] = dataset[i].replace(u' по коридору ', '  ')
        dataset[i] = dataset[i].replace(u' при нагрузк ', '  ')

        # синонимы

        dataset[i] = dataset[i].replace(u'не беспокоят', ' отрицает  ')
        dataset[i] = dataset[i].replace(u'болевой синдром', 'боль ')
        dataset[i] = dataset[i].replace(u'не ощущает', ' отрицает  ')
        dataset[i] = dataset[i].replace(u'не отмечает', ' отрицает  ')
        dataset[i] = dataset[i].replace(u' пастозность ', ' отечность  ')
        dataset[i] = dataset[i].replace(u' сжимающие ', ' давящие  ')
        dataset[i] = dataset[i].replace(u' нк ', ' носовые_кровотечения  ')
        dataset[i] = dataset[i].replace(u'не отмечала', ' отрицает  ')
        dataset[i] = dataset[i].replace(u' нет ', ' отрицает  ')
        dataset[i] = dataset[i].replace(u'в режитме стационара ', '  ')

        # меняем формы

        dataset[i] = dataset[i].replace(u' одышки', ' одышка ')
        dataset[i] = dataset[i].replace(u' плохим ', ' плохое  ')
        dataset[i] = dataset[i].replace(u' плохой ', ' плохое  ')
        dataset[i] = dataset[i].replace(u' плохой ', ' плохое  ')
        dataset[i] = dataset[i].replace(u'самочувствием', 'самочувствие ')
        dataset[i] = dataset[i].replace(u'общим ', 'общее  ')
        # dataset[i] = dataset[i].replace(u'общ.', 'общее ')
        dataset[i] = dataset[i].replace(u'боли ', 'боль  ')
        dataset[i] = dataset[i].replace(u'болей ', 'боль  ')
        dataset[i] = dataset[i].replace(u'шумы ', 'шум  ')
        dataset[i] = dataset[i].replace(u'шумит ', 'шум  ')
        # dataset[i] = dataset[i].replace(u'одышку ', 'одышка  ')
        # dataset[i] = dataset[i].replace(u' одышку', ' одышка ')
        dataset[i] = dataset[i].replace(u' голоса', ' голос ')
        dataset[i] = dataset[i].replace(u' сиплый', ' осиплость ')
        dataset[i] = dataset[i].replace(u' приступы', ' приступ ')
        dataset[i] = dataset[i].replace(u' мурашек', ' мурашки ')
        dataset[i] = dataset[i].replace(u' учащенного', ' учащенное ')
        dataset[i] = dataset[i].replace(u' сердцебиений', ' сердцебиение  ')
        dataset[i] = dataset[i].replace(u' сердцебиения', ' сердцебиение  ')
        dataset[i] = dataset[i].replace(u' предъявляла', ' предъявляет ')
        dataset[i] = dataset[i].replace(u' головную', ' головная ')
        dataset[i] = dataset[i].replace(u'умеренную ', 'умеренная  ')
        dataset[i] = dataset[i].replace(u'нижних понечностях', 'нижняя конечность  ')
        dataset[i] = dataset[i].replace(u'нижней понечности', 'нижняя конечность  ')
        dataset[i] = dataset[i].replace(u'не описывает', 'отрицает ')
        dataset[i] = dataset[i].replace(u'не описыват', 'отрицает ')
        dataset[i] = dataset[i].replace(u'не было', 'отрицает ')
        dataset[i] = dataset[i].replace(u'болезненность', 'боль ')
        dataset[i] = dataset[i].replace(u'болевого синдрома', 'боль ')
        dataset[i] = dataset[i].replace(u'повышение давления', 'повышение артериального давления ')
        dataset[i] = dataset[i].replace(u'давящий ', 'давящие  ')
        dataset[i] = dataset[i].replace(u'не беспокоили', 'отрицает ')
        dataset[i] = dataset[i].replace(u'не беспокоят', 'отрицает ')
        dataset[i] = dataset[i].replace(u'не испытывает', 'отрицает ')
        dataset[i] = dataset[i].replace(u'тяжести ', 'тяжесть  ')
        dataset[i] = dataset[i].replace(u'нарушений ', 'нарушения  ')
        dataset[i] = dataset[i].replace(u' не бепокоят', ' отрицает ')
        dataset[i] = dataset[i].replace(u' гр кл ', ' грудной клетке  ')
        dataset[i] = dataset[i].replace(u'сжимающие ', 'давящие  ')
        dataset[i] = dataset[i].replace(u'ангнозного ', 'ангиозного  ')
        dataset[i] = dataset[i].replace(u'не описыывает ', 'отрицает  ')
        dataset[i] = dataset[i].replace(u'не беспокоит', 'отрицает  ')
        dataset[i] = dataset[i].replace(u'боль в правом подреберье', 'боль_в_правом_подреберье ')
        dataset[i] = dataset[i].replace(u'гр клетки', 'грудной клетки ')
        dataset[i] = dataset[i].replace(u'при вдохе', 'при_вдохе ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли в покое', 'ангинозные_боли ')
        dataset[i] = dataset[i].replace(u'верхнюю конечность', 'левую руку ')
        dataset[i] = dataset[i].replace(u'анамнеза', 'анамнез ')
        dataset[i] = dataset[i].replace(u'анамнезом', 'анамнез ')
        dataset[i] = dataset[i].replace(u'анамнезе', 'анамнез ')
        dataset[i] = dataset[i].replace(u' болезни ', ' болезнь  ')
        dataset[i] = dataset[i].replace(u' больнице ', ' больница  ')
        dataset[i] = dataset[i].replace(u' больницу ', ' больница  ')
        dataset[i] = dataset[i].replace(u' был ', '  ')
        dataset[i] = dataset[i].replace(u' была ', '  ')
        dataset[i] = dataset[i].replace(u' были ', '  ')
        dataset[i] = dataset[i].replace(u' было ', '  ')


        # рана

        dataset[i] = dataset[i].replace(u'области послеоперационной раны', 'области_послеоперационной_раны ')
        dataset[i] = dataset[i].replace(u'боль в области_послеоперационной_раныы',
                                                'боль_области_послеоперационной_раны ')
        dataset[i] = dataset[i].replace(u'боль в области п о раны', 'боль_в_области_послеоперационной_раны ')

        # сокращения
        dataset[i] = dataset[i].replace(u' фн ', ' физическая_нагрузка  ')
        dataset[i] = dataset[i].replace(u' фн ', ' физическая_нагрузка  ')
        # dataset[i] = dataset[i].replace(u'ф.н.', 'физическая_нагрузка  ')
        # dataset[i] = dataset[i].replace(u'гр.кл.', 'грудная клетка  ')
        dataset[i] = dataset[i].replace(u'шаткость походки', 'шаткость_походки ')

        dataset[i] = dataset[i].replace(u' жалобб нет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'"', '  ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалоб нет ', 'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалоб не предъявляет', 'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалоб не представляет', 'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'жалоб на момент осмотра не предъявляет', 'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'при поступлении жалоб не предъявляет', 'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'на момент осмотра не предъявляет', 'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалоб не предьявляет', 'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалоб не предъявляет', ' на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u' в настоящее время нет', ' на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб не предявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб нет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб нет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'на момет осмотра не предъявляет', 'на_момент_осмотра_жалоб_нет ')

        dataset[i] = dataset[i].replace(u'не предьявляет по тяжести состояния', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб не предьявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб не предъявяет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб не паредлставляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'без жалоб ', 'на_момент_осмотра_жалоб_нет ')

        dataset[i] = dataset[i].replace(u'на_момент_осмотра_жалоб_нет на_момент_осмотра_жалоб_нет',
                                                'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'и анамнезом ознаковлены.', ' ')

        # на момент осмотра

        dataset[i] = dataset[i].replace(u'на момент осмотра жалоб актвивно не предъявляет',
                                                'на_момент_осмотра_жалобы_неактивно ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалоб активно не предъявляет',
                                                'на_момент_осмотра_жалобы_неактивно ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалобы активно не предъявляет',
                                                'на_момент_осмотра_жалобы_неактивно ')
        dataset[i] = dataset[i].replace(u'при поступлении жалоб не предъявляет',
                                                'на_момент_осмотра_жалобы_неактивно ')
        dataset[i] = dataset[i].replace(u'на моменнт осмотра жалоб активно не предъявляет',
                                                'на_момент_осмотра_жалобы_неактивно ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалоб активно не преъявляет',
                                                'на_момент_осмотра_жалобы_неактивно ')
        dataset[i] = dataset[i].replace(u'жалоб активно не предъявляет', 'на_момент_осмотра_жалобы_неактивно ')
        dataset[i] = dataset[i].replace(u'на момент осмотра активно не предъявляет',
                                                'на_момент_осмотра_жалобы_неактивно ')

        dataset[i] = dataset[i].replace(u'жалоб нет ', 'на_момент_осмотра_жалоб_нет  ')
        dataset[i] = dataset[i].replace(u'. жалоб_не_предъявляет. . жалоб_не_предъявляет.', 'жалоб_не_предъявляет ')
        dataset[i] = dataset[i].replace(u'// ', ' ')
        dataset[i] = dataset[i].replace(u'- ', '  ')
        dataset[i] = dataset[i].replace(u'  ', '  ')
        dataset[i] = dataset[i].replace(u'дата время ', ' ')
        dataset[i] = dataset[i].replace(u' время', '  ')
        dataset[i] = dataset[i].replace(u' вночное', '  ')
        dataset[i] = dataset[i].replace(u' в ночное', '  ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалобы на ', ' ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалобы на ', ' ')
        dataset[i] = dataset[i].replace(u'сбор жалоб и анамнеза затруднителен ',
                                                'сбор_жалоб_и_анамнеза_затруднителен ')
        dataset[i] = dataset[i].replace(u' жалоб_не_предъявляет жалоб_не_предъявляет', 'жалоб_не_предъявляет ')
        dataset[i] = dataset[i].replace(u'жалоб_не_предъявляет жалоб_не_предъявляет.', 'жалоб_не_предъявляет ')
        dataset[i] = dataset[i].replace(u'жалоб_не_предъявляет жалоб_не_предъявляет', 'жалоб_не_предъявляет ')
        dataset[i] = dataset[i].replace(u' на_момент_осмотра_жалоб_нет на_момент_осмотра_жалоб_нет',
                                                ' на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'при потуплении жалоб_не_предъявляет при потуплении жалоб_не_предъявляет',
                                                'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб_не_предъявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'активно жалобы не предъявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'активно не предъявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'на момент осмотра жалобы не предъявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'на_момент_осмотра_жалоб_нет  на_момент_осмотра_жалоб_нет.',
                                                'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'активно жалоб на предъявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'на_момент_осмотра_жалоб_нет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'на_момент_осмотра_жалоб_нет на_момент_осмотра_жалоб_нет',
                                                'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб активно не предьявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб не предяъвляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'без активных жалоб', 'на_момент_осмотра_жалоб_нет ')

        dataset[i] = dataset[i].replace(u'на_момент_осмотра_жалоб_нет', ' на_момент_осмотра_жалоб_нет ')

        # dataset[i] = dataset[i].replace(u'.. ', '  ')

        # ад

        dataset[i] = dataset[i].replace(u'повышение артериального давления отрицает',
                                                ' повышение_артериального_давления_отрицает ')
        dataset[i] = dataset[i].replace(u'повышение артериального давления',
                                                ' повышение_уровня_артериального_давления ')
        dataset[i] = dataset[i].replace(u' повышение ад отрицает',
                                                ' повышение_уровня_артериального_давления_отрицает ')
        dataset[i] = dataset[i].replace(u' подъемы ад ', ' повышение_уровня_артериального_давления_отрицает ')
        dataset[i] = dataset[i].replace(u' повышение ад отрифает',
                                                ' повышение_уровня_артериального_давления_отрицает ')
        dataset[i] = dataset[i].replace(u' повышения ад отрицает',
                                                ' повышение_уровня_артериального_давления_отрицает ')
        dataset[i] = dataset[i].replace(u'повышенных цифрах ад', 'повышение_уровня_артериального_давления_отрицает ')
        dataset[i] = dataset[i].replace(u'подъем ад ', ' повышение_уровня_артериального_давления ')
        dataset[i] = dataset[i].replace(u' уровня ад ', ' уровеня_артериального_давления ')
        dataset[i] = dataset[i].replace(u' повышение ад ', ' повышение_уровня_артериального_давления ')
        dataset[i] = dataset[i].replace(u' повышение ад', ' повышение_уровня_артериального_давления ')
        dataset[i] = dataset[i].replace(u' повышения ад', ' повышение_уровня_артериального_давления ')
        dataset[i] = dataset[i].replace(u'снижением ад ', 'снижение_уровня_артериального_давления  ')
        dataset[i] = dataset[i].replace(u'снижение ад', 'снижение_уровня_артериального_давления ')
        dataset[i] = dataset[i].replace(u'понижение_ад ', 'снижение_уровня_артериального_давления  ')
        dataset[i] = dataset[i].replace(u'снижение_ад ', 'снижение_уровня_артериального_давления  ')
        dataset[i] = dataset[i].replace(u' повышенеие ад', ' повышение_уровня_артериального_давления ')
        dataset[i] = dataset[i].replace(u' повышении ад', ' повышение_уровня_артериального_давления ')
        dataset[i] = dataset[i].replace(u' лабильность ад', ' лабильность_артериального_давления ')
        dataset[i] = dataset[i].replace(u'повышение ад ', ' повышение_уровня_артериального_давления  ')

        # уши
        dataset[i] = dataset[i].replace(u'снижение слуха', 'снижение слуха ')

        dataset[i] = dataset[i].replace(u'ухудшение слуха', 'снижение слуха ')

        # мочеполовая
        dataset[i] = dataset[i].replace(u' затрудненное мочеиспускание', ' затрудненное_мочеиспускание ')
        dataset[i] = dataset[i].replace(u' болезненное мочеиспускание', ' болезненное_мочеиспускание ')

        dataset[i] = dataset[i].replace(u' болезненное мочеспускание', 'болезненное_мочеиспускание ')
        dataset[i] = dataset[i].replace(u'боль при мочеиспускании', 'болезненное_мочеиспускание ')
        dataset[i] = dataset[i].replace(u' учащенное затрудненное_мочеиспускание',
                                                ' учащенное_затрудненное_мочеиспускание ')
        dataset[i] = dataset[i].replace(u'отсутствие диуреза', 'отсутствие_диуреза ')
        dataset[i] = dataset[i].replace(u'отсутствие самостоятельного мочеиспускания', 'отсутствие_диуреза ')
        dataset[i] = dataset[i].replace(u'отсутствие диуреза', 'отсутствие_диуреза ')
        dataset[i] = dataset[i].replace(u'отсутствие самостоятельного мочеиспускания', 'отсутствие_диуреза ')
        dataset[i] = dataset[i].replace(u'отсутсвие самостоятельного мочеиспускания', 'отсутствие_диуреза ')

        dataset[i] = dataset[i].replace(u'учащенное мочеиспускание', 'учащенное_мочеиспускание ')
        dataset[i] = dataset[i].replace(u'вялая струя мочи', 'вялая_струя_мочи ')
        dataset[i] = dataset[i].replace(u'дискомфорт при мочеиспускании', 'затрудненное_мочеиспускание ')
        dataset[i] = dataset[i].replace(u'учащенное болезненное_мочеиспускание',
                                                'учащенное мочеиспускание болезненное_мочеиспускание ')

        # сердце

        dataset[i] = dataset[i].replace(u' перебои в работе сердца', ' перебои_в_работе_сердца ')
        dataset[i] = dataset[i].replace(u'дискомфорт в области сердца', ' дискомфорт_за_грудиной ')

        dataset[i] = dataset[i].replace(u'дискомфорт за грудиной', 'дискомфорт_за_грудиной ')
        dataset[i] = dataset[i].replace(u'дискомфорт в грудной клетке', 'дискомфорт_за_грудиной ')
        dataset[i] = dataset[i].replace(u'дискомфрта за грудиной', 'дискомфорт_за_грудиной ')
        dataset[i] = dataset[i].replace(u'боль_за грудиной', 'боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'боль в грудной кретке', 'боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'боль в грудной клетки слева', 'боль_за_грудиной ')

        dataset[i] = dataset[i].replace(u' давления за грудиной', ' даващие_боли_за_грудиной ')
        dataset[i] = dataset[i].replace(u' давящими болями за грудиной', ' даващие_боли_за_грудиной ')
        dataset[i] = dataset[i].replace(u' давящие боли за грудиной', ' даващие_боли_за_грудиной ')
        dataset[i] = dataset[i].replace(u' дискомфорта за грудиной', ' дискомфорт_за_грудиной ')
        dataset[i] = dataset[i].replace(u'боль ноюще-колющего характера за грудиной', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'боль давящего характера за грудиной', 'давящая_боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'грудиной давящего характера', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'жжение за грудиной', 'жжение_за_грудиной ')
        dataset[i] = dataset[i].replace(u'жжения загрудиной', 'жжение_за_грудиной ')
        dataset[i] = dataset[i].replace(u'жжения за грудиной', 'жжение_за_грудиной ')

        dataset[i] = dataset[i].replace(u'жжение в левой половине грудной клетке', 'жжение_за_грудиной ')
        dataset[i] = dataset[i].replace(u'жжение в грудной клетке', 'жжение_за_грудиной ')
        dataset[i] = dataset[i].replace(u'дискомфорт за грудиной', ' дискомфорт_за_грудиной ')
        dataset[i] = dataset[i].replace(u' боль за грудиной', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'загрудинные боль', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'загрудинных боль', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'дискомфорт за грудиной ', 'дискомфорт_за_грудиной  ')
        dataset[i] = dataset[i].replace(u'боль за грудиной', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'боль за грудинной', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'левой половине грудной клетки', ' левой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'боль в левой половине грудной клетке',
                                                'боль_в_левой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'боль в левой половине грудной клетке отрицает',
                                                'боль_в_левой_половине_грудной_клетки_отрицает ')
        dataset[i] = dataset[i].replace(u'болью в левой половине грудной клетке',
                                                'боль_в_левой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'боль давяще-ноющая в левой половине грудной клетке',
                                                'боль_в_левой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'боль сжимающего характера в левой_половине_грудной_клетки',
                                                'боль_в_левой_половине_грудной_клетки ')

        dataset[i] = dataset[i].replace(u'дискомфорт в левой половине грудной клетке',
                                                'дискомфорт_в_левой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'трепыхание в левой половине грудной клетке',
                                                'дискомфорт_в_левой_половине_грудной_клетки ')

        dataset[i] = dataset[i].replace(u'дискомфорт в левой_половине_грудной_клетки',
                                                'дискомфорт_в_левой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'боль в левой половине грудной клетки',
                                                'боль_в_левой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'боль в правой половине грудной клетки',
                                                'боль_в_правой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'боль в области грудины', ' боль_за_грудиной ')

        dataset[i] = dataset[i].replace(u'боли в грудной клетке отрицает', 'боль_за_грудиной_отрицает ')
        dataset[i] = dataset[i].replace(u'боли в грудной клетке', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'перебоев в работе сердца', 'перебои_в_работе_сердца ')
        dataset[i] = dataset[i].replace(u'нарушения ритма сердца', 'нарушение_ритма ')

        dataset[i] = dataset[i].replace(u'загрудинные боли', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'дискомфорты в грудной клетке', 'дискомфорт_за_грудиной ')
        dataset[i] = dataset[i].replace(u'осмотр дежурного реаниматолога', ' ')
        dataset[i] = dataset[i].replace(u'купирующиеся в покое', 'купирующиеся_в_покое ')
        dataset[i] = dataset[i].replace(u'купирующуюся в покое', 'купирующиеся_в_покое ')
        dataset[i] = dataset[i].replace(u'купирующиеся после остановки через минут через минут при приеме нг',
                                                'купирующиеся_в_покое' 'купируется_нитратами ')

        dataset[i] = dataset[i].replace(u'учащенных сердебиений', 'нарушение_ритма ')

        dataset[i] = dataset[i].replace(u'проходят в покое', 'купирующиеся_в_покое ')
        dataset[i] = dataset[i].replace(u'боль в грудной клекте отрицает', ' боль_за_грудиной_отрицает ')
        dataset[i] = dataset[i].replace(u'боль в грудной клекте', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'дискомфорт в груднйо клетке', ' дискомфорт_за_грудиной ')
        dataset[i] = dataset[i].replace(u'неприятные в грудной клетке', ' дискомфорт_за_грудиной ')
        dataset[i] = dataset[i].replace(u'боль в груди', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'болей в области сердца', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'боль в области сердца', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'боль в сердце', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'боль давящего сжимающего характера', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'боли в сердце отрицает', 'боль_в_области_сердца_отрицает ')
        dataset[i] = dataset[i].replace(u'боль в грудной клетке', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'боль в области сердца', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'боль в области сердца', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'учащенное сердцебиение', 'учащенное_сердцебиение ')
        dataset[i] = dataset[i].replace(u'ритмичного сердцебиение', 'учащенное_сердцебиение ')
        dataset[i] = dataset[i].replace(u'тяжесть за грудиной', 'тяжесть_за_грудиной ')
        dataset[i] = dataset[i].replace(u'нарушения ритма отрицает', 'нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(u'нарушения ритма не ощущает', 'нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(u'боль_в_области_сердца отрицает', 'боль_в_области_сердца_отрицает ')
        dataset[i] = dataset[i].replace(u'частого сердцебиение', 'учащенное_сердцебиение ')
        dataset[i] = dataset[i].replace(u'боль_в_области_сердца нет', 'боль_в_области_сердца_отрицает ')
        dataset[i] = dataset[i].replace(u'учащенное неритмичное сердцебиение', 'учащенное_сердцебиение ')
        # dataset[i] = dataset[i].replace(u'приступ сердцебиение', 'учащенное_сердцебиение ')
        dataset[i] = dataset[i].replace(u'боли_за_грудиной отрицает', 'боль_в_области_сердца_отрицает ')
        dataset[i] = dataset[i].replace(u'приступов сердцебиение не было', 'учащенное_сердцебиение_отрицает ')
        dataset[i] = dataset[i].replace(u'приступов сердцебиение не было', 'учащенное_сердцебиение_отрицает ')
        dataset[i] = dataset[i].replace(u'боль внутри грудной клетки', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'ангинозные учащенное_сердцебиение отрицает',
                                                'нарушение_ритма_отрицает ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'иррадиацией в левую руку', 'иррадиация_в_левую_руку ')
        dataset[i] = dataset[i].replace(u'с иррадиацией в левое плечо', 'иррадиация_в_левое_плечо ')
        dataset[i] = dataset[i].replace(u'иррадиациев в левую лопатку', 'иррадиация_в_левое_лопатку ')
        dataset[i] = dataset[i].replace(u'иррадиацией в обе руки', 'иррадиация_в_обе_руки ')
        dataset[i] = dataset[i].replace(u'иррадиацией в нижнюю челюсть', 'иррадиация_в_нижнюю_челюсть ')
        dataset[i] = dataset[i].replace(u'иррадиация_в_левое_плечо и левую руку',
                                                'иррадиация_в_левое_плечо иррадиация_в_левую_руку ')
        dataset[i] = dataset[i].replace(u'иррадиация в левую руку', 'иррадиация_в_левую_руку ')
        dataset[i] = dataset[i].replace(u'иррадиирующие в левую руку', 'иррадиация_в_левую_руку ')
        dataset[i] = dataset[i].replace(u'иррадицией в левую руку', 'иррадиация_в_левую_руку ')
        dataset[i] = dataset[i].replace(u'иррадиацией в левую левую руку', 'иррадиация_в_левую_руку ')
        dataset[i] = dataset[i].replace(u'иррадиацией в межлопаточную область и в левую руку',
                                                'иррадиация_в_левую_руку иррадиация_в_межлопаточную_область ')
        dataset[i] = dataset[i].replace(u'иррадиацией в межлопаточную область',
                                                'иррадиация_в_межлопаточную_область ')

        dataset[i] = dataset[i].replace(u'нарушений ритма не отмечает', 'нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(u'сердечная недостаточность', 'сердечная_недостаточность ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли одышка сердцебиение отрицает',
                                                'ангинозные_боли одышку_отрицает нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(u'сердцебиение отрицает', 'нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(u'перебои отрицает', 'перебои_в_работе_сердца_отрицает  ')
        dataset[i] = dataset[i].replace(u'перебои_в_работе_сердца отрицает', 'перебои_в_работе_сердца_отрицает  ')
        dataset[i] = dataset[i].replace(u' перебои в работе сердца', ' боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'перебои в работе сердца', ' нарушение_ритма ')
        dataset[i] = dataset[i].replace(u'жжения в грудной клетке', 'жжение_за_грудиной ')
        dataset[i] = dataset[i].replace(u'жжение в груди', ' жжение_за_грудиной ')

        dataset[i] = dataset[i].replace(u'жгучие боль_за_грудиной', 'жжение_за_грудиной ')
        dataset[i] = dataset[i].replace(u'давящая ', 'давящие  ')
        dataset[i] = dataset[i].replace(u'давящие боль_в_области_сердца', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'давящие боль в загрудинной области', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'сдавления в грудной клетке', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'боль_в_области_сердца сжимающего характера', 'боль_в_области_сердца  ')
        dataset[i] = dataset[i].replace(u'давящие боль_за_грудиной', 'боль_за_грудиной ')
        dataset[i] = dataset[i].replace(u'коронарные боль отрицает', 'коронарную_боль_отрицает ')
        dataset[i] = dataset[i].replace(u'коронарные боль', 'коронарная_боль ')
        # dataset[i] = dataset[i].replace(u' сердцебиение', ' учащенное_сердцебиение ')
        dataset[i] = dataset[i].replace(u'ускоренного сердцебиение', 'учащенное_сердцебиение ')
        dataset[i] = dataset[i].replace(u'ускоренное сердцебиение', 'учащенное_сердцебиение ')
        dataset[i] = dataset[i].replace(u'учащение учащенное_сердцебиение', 'учащенное_сердцебиение ')
        dataset[i] = dataset[i].replace(u'судороги в икроножных мышцах', 'судороги_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'боль в икроножных мышцах', 'боль_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'судорог в икроножных мышцах', 'судороги_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'судороги в нижних конечностях', 'судороги_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'судороги икроножных мышц', 'судороги_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'сжатие_за_грудиной отрицает', 'сжатие_за_грудиной_отрицает ')

        # сосуды

        dataset[i] = dataset[i].replace(u'отеков н конечностей', 'отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u' отеки нижних конечностей', ' отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u'отеки стоп', 'отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u' отеки нижняя конечность', ' отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u' отеки нижняя конечность', ' отеки_нижних_конечностей_отрицает ')
        dataset[i] = dataset[i].replace(u' отеки на ногах', ' отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u' отеки ног', ' отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u'отеки_нижних_конечностей отрицает', 'отеки_нижних_конечностей_отрицает ')
        dataset[i] = dataset[i].replace(u' отеки ног', ' отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u'отек нижней конечности', 'отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u'отечность нижних конечностей', 'отеки_нижних_конечностей ')
        dataset[i] = dataset[i].replace(u'отеки отрицает', 'отеки_отрицает ')
        dataset[i] = dataset[i].replace(u'отеков нет', 'отеки_отрицает ')

        # дыхание

        dataset[i] = dataset[i].replace(u'влажного кашля', 'влажный_кашель ')
        dataset[i] = dataset[i].replace(u'кашель влажный', 'влажный_кашель ')
        dataset[i] = dataset[i].replace(u'влажный кашель', 'влажный_кашель ')

        dataset[i] = dataset[i].replace(u'сухой кашель', 'сухой_кашель ')
        dataset[i] = dataset[i].replace(u'нехватки воздуха', 'нехватка_воздуха ')
        dataset[i] = dataset[i].replace(u'нехваткой воздуха', 'нехватка_воздуха ')
        dataset[i] = dataset[i].replace(u'нехватки воздуха нет', 'нехватку_воздуха_отрицает ')
        dataset[i] = dataset[i].replace(u'кровохарканье отрицает', ' кровохарканье_отрицает ')
        dataset[i] = dataset[i].replace(u'кровохарканья отрицает', ' кровохарканье_отрицает ')
        dataset[i] = dataset[i].replace(u'без кровохарканья', ' кровохарканье_отрицает ')

        dataset[i] = dataset[i].replace(u'одышку отрицает', 'одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'одышку в покое', 'одышку_в_покое ')
        dataset[i] = dataset[i].replace(u'одышки в покое нет', 'одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'кашель с отхождением мокроты', 'кашель_с_отхождением_мокроты ')
        dataset[i] = dataset[i].replace(u'одышки нет', 'одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'умеренная одышка', 'умеренная_одышка ')
        dataset[i] = dataset[i].replace(u'одышка при ходьбе', 'одышка_при_ходьбе ')
        dataset[i] = dataset[i].replace(u'одышка при незначительных нагрузках', 'одышка_при_ходьбе ')
        dataset[i] = dataset[i].replace(u'одышка при ускорении темпа ходьбы', 'одышка_при_физической_нагрузке ')

        dataset[i] = dataset[i].replace(u'одышка_при_ходьбе отрицает', 'одышку_при_ходьбе_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка_при_ходьбе нет', 'одышку_при_ходьбе_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка при физическая_нагрузка', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при физич нагрузке', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при быстрой ходьбе', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при ходьбе', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при фн', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при физическая_нагрузка отрицает',
                                                'одышку_при_физической_нагрузке_отрицает ')
        dataset[i] = dataset[i].replace(u'нехватку воздуха', 'одышку_в_покое ')
        dataset[i] = dataset[i].replace(u'одышка при ходъбе', 'одышка_при_ходьбе ')
        dataset[i] = dataset[i].replace(u'одышка в покое отрицает', 'одышку_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка отрицает', 'одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка при подъеме', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'заложенность носа', 'заложенность_носа ')
        dataset[i] = dataset[i].replace(u'заложенный нос', 'заложенность_носа ')
        dataset[i] = dataset[i].replace(u'кашель с мокротой', 'кашель_с_мокротой ')
        dataset[i] = dataset[i].replace(u'кашель_с_мокротой', 'кашель_с_мокротой ')
        dataset[i] = dataset[i].replace(u'кашель_с_мокротой отрицает', 'кашель_с_мокротой_отрицает ')

        dataset[i] = dataset[i].replace(u'одышка при небольшой физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при минимальной физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при минимальной ф н', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при минимальных физических нагрузках',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при физической нграузке', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'кашель со светлой мокротой', 'кашель_с_мокротой ')
        dataset[i] = dataset[i].replace(u'одышка при умеренных физических нагрузках',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка не беспокоит', 'одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка при физической нагрузке', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при физической нагрузке', 'одышка_при_физической_нагрузке ')

        dataset[i] = dataset[i].replace(u'одышка при небоьшой', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку в покое ангинозные_боли_отрицает',
                                                'одышку_в_покое_отрицает ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка при незначительной физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при незначит нагрузке', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при небольших физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при небольших физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка инспираторного характера', 'одышка_инспираторного_характера ')
        dataset[i] = dataset[i].replace(u'одышка больше инспиратортного', 'одышка_инспираторного_характера ')
        dataset[i] = dataset[i].replace(u'одышка затрудненный вдох', 'одышка_инспираторного_характера ')
        dataset[i] = dataset[i].replace(u'одышка при минимальной нагрузке', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка в положении лежа', 'одышка_в_покое ')
        dataset[i] = dataset[i].replace(u'одышка при умеренной физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при умеренной физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при небльшой физ нагрузке', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при привычной физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при небольшой физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при незначительной нагрузке', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при незначительной физическая_нагрузка',
                                                'одышка_при_физической_нагрузке ')

        dataset[i] = dataset[i].replace(u'одышка при ускорении шага', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка нет', 'одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка в покое нет', 'одышку_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка в покое', 'одышка_в_покое ')
        dataset[i] = dataset[i].replace(u'кашель отрицает', 'кашель_отрицает ')
        dataset[i] = dataset[i].replace(u'кашель нет', 'кашель_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка при умеренной физической нагрузке',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при незначительной физической нагрузке',
                                                'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при незначительной фн', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышка при интенсивной фн', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'приступ удушья отрицает', 'приступы_удушья_отрицает ')
        dataset[i] = dataset[i].replace(u'приступы удушья отрицает', 'приступы_удушья_отрицает ')
        dataset[i] = dataset[i].replace(u'приступы удушья', 'приступы_удушья ')
        dataset[i] = dataset[i].replace(u'приступ удушья', 'приступы_удушья ')
        dataset[i] = dataset[i].replace(u' мин ', ' минимальной  ')
        dataset[i] = dataset[i].replace(u'при миним фн', 'при_минимальной_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при умеренной физическая_нагрузка отрицает', 'одышку_отрицает ')

        dataset[i] = dataset[i].replace(u'синкопальные пресинкопальные состояния отрицает',
                                                'синкопальные_состояния_отрицает пресинкопальные_состояния_отрицает ')

        dataset[i] = dataset[i].replace(u'пренсикопального и синкопального состояния отрицает',
                                                'синкопальные_состояния_отрицает пресинкопальные_состояния_отрицает ')
        dataset[i] = dataset[i].replace(u'пресинкопальные состояния отрицает', 'пресинкопальные_состояния_отрицает ')
        dataset[i] = dataset[i].replace(u'пресинкопальные состояния отрицает', 'пресинкопальные_состояния_отрицает ')
        dataset[i] = dataset[i].replace(u'синкопальные состояния отрицает', 'синкопальные_состояния_отрицает ')
        dataset[i] = dataset[i].replace(u'неритмичное сердцебиение синкопальные_состояния_отрицает',
                                                'нарушение_ритма_отрицает синкопальные_состояния_отрицает ')
        dataset[i] = dataset[i].replace(u'дискомфорт боль_в_области_сердца нарушение_ритма_отрицает ',
                                                'боль_в_области_сердца_отрицает нарушение_ритма_отрицает  ')

        dataset[i] = dataset[i].replace(u'проходит в покое', 'купируется_в_покое ')
        dataset[i] = dataset[i].replace(u'купируется после остановки', 'купируется_в_покое ')
        dataset[i] = dataset[i].replace(u'пресинкопальные состояния', 'пресинкопальные_состояния ')

        dataset[i] = dataset[i].replace(u'боль ангиозного характера отрицает', 'ангиозную_боль_отрицает ')

        # глаза
        dataset[i] = dataset[i].replace(u'двоение в глазах', 'двоение_в_глазах ')
        dataset[i] = dataset[i].replace(u'мурашки перед глазами', 'мурашки_перед_глазами ')
        dataset[i] = dataset[i].replace(u'потемнение в глазах', 'потемнение_в_глазах_отрицает ')
        dataset[i] = dataset[i].replace(u'потемнение в нет', 'потемнение_в_глазах_отрицает ')
        dataset[i] = dataset[i].replace(u'потемнение в глазах', 'потемнение_в_глазах ')

        # слух
        dataset[i] = dataset[i].replace(u'шум в ушах', 'шум_в_ушах ')

        # вес
        dataset[i] = dataset[i].replace(u'вес стабилен', 'вес_стабилен ')

        # двигательная

        dataset[i] = dataset[i].replace(u' нога ', ' нижняя конечность  ')
        dataset[i] = dataset[i].replace(u' ног ', ' нижняя конечность  ')
        dataset[i] = dataset[i].replace(u' ноги ', ' нижняя конечность  ')
        dataset[i] = dataset[i].replace(u' ноге ', ' нижняя конечность  ')
        dataset[i] = dataset[i].replace(u'боль в нижняя конечность', 'боль_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'боль в нижних конечностях', 'боль_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'боль в ногах', 'боль_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'боль в коленных суставах', 'боль_в_коленных_суставах ')
        dataset[i] = dataset[i].replace(u'боль в коленнях', 'боль_в_коленных_суставах ')
        dataset[i] = dataset[i].replace(u'боль в икроножной мышце', 'боль_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'боль в левой икроножной мышце', 'боль_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'боль в правой икроножной мышце', 'боль_в_нижних_конечностях ')
        dataset[i] = dataset[i].replace(u'тяжесть в ногах', 'слабость_в_ногах ')
        dataset[i] = dataset[i].replace(u'слабость в ногах', 'слабость_в_ногах ')

        # живот
        dataset[i] = dataset[i].replace(u'боль внизу живота', 'боль_внизу_живота ')

        dataset[i] = dataset[i].replace(u'ангинозные приступ', 'ангинозные боли ')
        dataset[i] = dataset[i].replace(u'ангинозные боли', 'ангинозные_боли ')
        dataset[i] = dataset[i].replace(u'ангинозные боли отрицает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'отсутствия ангинозных приступов', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозных приступов отрицает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'отсутствие ангинозных приступов', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли не беспокоят', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные приступы отрицает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'нет ангинозные_боли', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозных болей нет', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли отрицает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'боли ангинозного характера', 'ангинозные_боли ')
        dataset[i] = dataset[i].replace(u'ангинозных боль нет', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли_отрицает. ангинозные_боли_отрицает.',
                                                'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозных боль не испытывал', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боль', 'ангинозные боли ')
        dataset[i] = dataset[i].replace(u'ангинозные боли отрицает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозных боль не отмечает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли не описывает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные не описывает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозной боль отрицает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'боль ангинозного характера', 'ангинозные_боли ')
        dataset[i] = dataset[i].replace(u'ангинозные боли в покое отрицает', 'ангинозные_боли_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли в покое отрицает', 'ангинозные_боли_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли и одышку_отрицает',
                                                'ангинозные_боли_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли не описывает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозных приступов нет', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли одышку_отрицает не_лихорадит',
                                                ' ангинозные_боли_отрицает одышку_отрицает не_лихорадит ')
        dataset[i] = dataset[i].replace(u'жидкий стул', ' жидкий_стул ')
        dataset[i] = dataset[i].replace(u'ангинозных боль', ' ангинозные_боли ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли отрицает', 'ангинозные_боли_отрицает ')

        dataset[i] = dataset[i].replace(u'ангинозные боли в покое', 'ангинозные_боли_в_покое ')

        dataset[i] = dataset[i].replace(u'жалоб не предъявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'не предъявляет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб не представляет', 'на_момент_осмотра_жалоб_нет ')

        dataset[i] = dataset[i].replace(u'купируется в покое', 'купируется_в_покое ')
        dataset[i] = dataset[i].replace(u'купируются в покое', 'купируется_в_покое ')

        # боль
        dataset[i] = dataset[i].replace(u'головная боль', 'головная_боль ')
        dataset[i] = dataset[i].replace(u'суставная боль', 'суставная_боль ')
        dataset[i] = dataset[i].replace(u'головные боль', 'головная_боль ')
        dataset[i] = dataset[i].replace(u'головный боль', 'головная_боль ')
        dataset[i] = dataset[i].replace(u'головную боль', 'головная_боль ')
        dataset[i] = dataset[i].replace(u'давящего характера', 'давящего_характера ')

        dataset[i] = dataset[i].replace(u'без нарастания', 'без_нарастания ')
        dataset[i] = dataset[i].replace(u'не лихорадит', ' не_лихорадит ')
        dataset[i] = dataset[i].replace(u' познабливание', 'лихорадит ')
        dataset[i] = dataset[i].replace(u' озноб', 'лихорадит ')

        dataset[i] = dataset[i].replace(u'катаральных явлений нет', 'катаральных_явлений_нет ')
        dataset[i] = dataset[i].replace(u'общую слабость', 'общая_слабость ')
        dataset[i] = dataset[i].replace(u'на слабость ', 'общая_слабость  ')

        dataset[i] = dataset[i].replace(u'общая слабость', 'общая_слабость ')
        dataset[i] = dataset[i].replace(u'выраженная слабость', 'общая_слабость ')
        dataset[i] = dataset[i].replace(u'выраженную слабость', 'общая_слабость ')
        dataset[i] = dataset[i].replace(u'изменение речи', 'изменение_речи ')
        dataset[i] = dataset[i].replace(u'нарушения речи', 'изменение_речи ')
        dataset[i] = dataset[i].replace(u'ухудшение речи', 'изменение_речи ')
        dataset[i] = dataset[i].replace(u'общая_общая_слабость', 'общая_слабость ')

        dataset[i] = dataset[i].replace(u' общая_слабость отрицает', 'общую_слабость_отрицает ')
        # dataset[i] = dataset[i].replace(u' слабость ', ' общая_слабость  ')
        dataset[i] = dataset[i].replace(u'боль в эпигастрии', 'боль_в_эпигастрии ')

        dataset[i] = dataset[i].replace(u'общается жестами', 'общается_жестами ')

        # Повторность
        dataset[i] = dataset[i].replace(u'не рецидив ', 'не_рецидив ')
        dataset[i] = dataset[i].replace(u'не рецидивирующая ', 'не_рецидив ')

        # общее состояние

        dataset[i] = dataset[i].replace(u'самочувствие хорошее', 'самочувствие_хорошее  ')
        dataset[i] = dataset[i].replace(u'самочувствие удовлетворительно', 'самочувствие_удовлетворительное ')
        dataset[i] = dataset[i].replace(u'самочувствие удовлетворительное', 'самочувствие_удовлетворительное ')
        dataset[i] = dataset[i].replace(u'плохое самочувствие', 'плохое_самочувствие ')
        dataset[i] = dataset[i].replace(u'общ слабость', 'общая_слабость ')
        dataset[i] = dataset[i].replace(u'общей слабостью', 'общая_слабость ')
        dataset[i] = dataset[i].replace(u'быстрая утомляемость', 'быстрая_утомляемость ')
        dataset[i] = dataset[i].replace(u'незначительная слабость', 'слабость ')
        dataset[i] = dataset[i].replace(u'небольшая слабость', 'слабость ')
        dataset[i] = dataset[i].replace(u'небольшая слабость', 'слабость ')
        dataset[i] = dataset[i].replace(u'небольшую слабость', 'слабость ')
        dataset[i] = dataset[i].replace(u'общую слаость', 'общую_слаость ')
        dataset[i] = dataset[i].replace(u'самочувствие лучше', 'самочувствие_улучшелось ')
        dataset[i] = dataset[i].replace(u'самочувствие улучшелось', 'самочувствие_улучшелось ')
        dataset[i] = dataset[i].replace(u'самочувствие стало лучше', 'самочувствие_улучшелось ')

        # dataset[i] = dataset[i].replace(u' слабость ', 'общая_слабость  ')
        dataset[i] = dataset[i].replace(u'повышенная утомляемость', 'быстрая_утомляемость ')
        dataset[i] = dataset[i].replace(u'самочувствие плохое', 'плохое_самочувствие ')
        dataset[i] = dataset[i].replace(u'чувствует себя хорошо', 'самочувствие_хорошее  ')
        dataset[i] = dataset[i].replace(u'повышенная потливость', 'повышенная_потливость ')
        dataset[i] = dataset[i].replace(u'повышенную потливость', 'повышенная_потливость ')
        dataset[i] = dataset[i].replace(u'ухудшение состояния', 'плохое_самочувствие ')
        dataset[i] = dataset[i].replace(u'потери сознания', 'потери_сознания ')
        dataset[i] = dataset[i].replace(u'обмороки ', 'потери_сознания ')
        dataset[i] = dataset[i].replace(u'обморочные состояния', 'потери_сознания ')
        dataset[i] = dataset[i].replace(u'обморочное состояние', 'потери_сознания ')
        dataset[i] = dataset[i].replace(u'потери_сознания отрицает', 'потери_сознания_отрицает ')
        dataset[i] = dataset[i].replace(u'обмороков ', 'потери_сознания  ')
        dataset[i] = dataset[i].replace(u'умеренные головокружения', 'головокружение ')
        dataset[i] = dataset[i].replace(u'головокружения', 'головокружение ')
        dataset[i] = dataset[i].replace(u'головокружений нет', 'головокружение_отрицает ')
        dataset[i] = dataset[i].replace(u'головокружение отрицает', 'головокружение_отрицает ')
        dataset[i] = dataset[i].replace(u'головокружение  отрицает', 'головокружение_отрицает ')
        dataset[i] = dataset[i].replace(u'головокружений ', 'головокружение  ')
        dataset[i] = dataset[i].replace(u'физнагрузке ', 'физической нагрузке  ')
        dataset[i] = dataset[i].replace(u'самочувствие неплохое', 'самочувствие_хорошее  ')
        dataset[i] = dataset[i].replace(u'нарушение сна', 'нарушение_сна ')
        dataset[i] = dataset[i].replace(u'плохое сон', 'нарушение_сна ')

        dataset[i] = dataset[i].replace(u'осиплость голос', 'осиплость_голоса ')

        dataset[i] = dataset[i].replace(u'повышение температуры тела до', 'повышение_температуры ')
        dataset[i] = dataset[i].replace(u'повышение температуры отрицает', 'повышение_температуры_отрицает ')
        dataset[i] = dataset[i].replace(u'повышенная температура', 'повышенная_температура ')
        dataset[i] = dataset[i].replace(u'повышенная_температура отрицает', 'повышенная_температура_отрицает ')
        dataset[i] = dataset[i].replace(u'повышенная_температура_отрицает', 'повышение_температуры_отрицает ')
        dataset[i] = dataset[i].replace(u'повышение температуры тела отрицает', 'повышение_температуры_отрицает ')
        dataset[i] = dataset[i].replace(u'повышение температуры до', 'повышение_температуры ')
        dataset[i] = dataset[i].replace(u'повышение температуры', 'повышение_температуры ')

        # положение
        dataset[i] = dataset[i].replace(u'лежит с низким изголовьем', 'лежит_с_низким_изголовьем ')
        dataset[i] = dataset[i].replace(u'спит с высоким изголовьем', 'лежит_с_низким_изголовьем ')
        dataset[i] = dataset[i].replace(u'спит с низким изголовьем', 'спит_с_низким_изголовьем ')

        # голова
        dataset[i] = dataset[i].replace(u'тяжесть в голове', 'тяжесть_в_голове ')
        dataset[i] = dataset[i].replace(u'шум в голове', 'шум_в_голове ')
        dataset[i] = dataset[i].replace(u'сухость во рту', 'сухость_во_рту ')
        dataset[i] = dataset[i].replace(u'боль в глотке', 'боль_в_глотке ')

        dataset[i] = dataset[i].replace(u'без иррадиации', 'иррадиации_нет ')
        dataset[i] = dataset[i].replace(u'иррадиации нет', 'иррадиации_нет ')
        dataset[i] = dataset[i].replace(u'иррадиация не отмечается', 'иррадиаци_нет ')

        # dataset.diagnapr = dataset.diagnapr.str.replace(u'\sсд$|\sсд\s|^сд\s|^сд$', u' сахарный_диабет  ')

        dataset[i] = dataset[i].replace(u'пре синкопе', 'пресинкопе ')
        dataset[i] = dataset[i].replace(u'купирующиеся покоем', 'купирующиеся_в_покое ')
        dataset[i] = dataset[i].replace(u'купирующееся в покое', 'купирующиеся_в_покое ')
        dataset[i] = dataset[i].replace(u'жалоб на_момент_осмотра_жалоб_нет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'удушья синкопе кровохарканье в анамнезе отрицает',
                                                'удушья_отрицает, кровохарканье_отрицает, синкопе_отрицает ')
        dataset[i] = dataset[i].replace(u' синкопе отрицает', ' синкопе_отрицает ')
        dataset[i] = dataset[i].replace(u' пресинкопе отрицает', ' пресинкопе_отрицает ')

        dataset[i] = dataset[i].replace(u'вр морошкина нв соловьёва нв', ' ')
        dataset[i] = dataset[i].replace(u'тдглебовской', ' ')
        dataset[i] = dataset[i].replace(u'осмотр перед кхо', ' ')

        dataset[i] = dataset[i].replace(u'ангинозные боли не_рецидивидивировали',
                                                'ангинозные_боли_не_рецидивидивировали ')
        dataset[i] = dataset[i].replace(u'ангинозные боли не_рецидивидивируют',
                                                'ангинозные_боли_не_рецидивидивировали ')
        dataset[i] = dataset[i].replace(u'жалоб не предъвляе', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'не предьявляет', 'на_момент_осмотра_жалоб_нет ')

        # длинное

        dataset[i] = dataset[i].replace(u'ангинозные_боли_в_покое и при умеренной физическая_нагрузка отрицает',
                                                'ангинозные_боли_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли одышка не отмечает',
                                                'ангинозные_боли_отрицает одышку_отрицает ')

        # Удаление

        dataset[i] = dataset[i].replace(u'  ', '  ')

        dataset[i] = dataset[i].replace(u'жалобы ', ' ')
        dataset[i] = dataset[i].replace(u'подъем до', ' ')
        dataset[i] = dataset[i].replace(u'на момент осмотра', ' ')
        dataset[i] = dataset[i].replace(u'этажа', ' ')
        dataset[i] = dataset[i].replace(u'этаж', ' ')
        dataset[i] = dataset[i].replace(u'поступает переводом из', ' ')
        dataset[i] = dataset[i].replace(u'вр морошкина нв зуева иб', ' ')
        dataset[i] = dataset[i].replace(u'при поступлени', ' ')
        dataset[i] = dataset[i].replace(u'пациентка ', ' ')
        dataset[i] = dataset[i].replace(u'пациент ', ' ')
        dataset[i] = dataset[i].replace(u'-на', ' ')
        dataset[i] = dataset[i].replace(u'вр морошкина нв ио', ' ')
        dataset[i] = dataset[i].replace(u'смирнова на', ' ')
        dataset[i] = dataset[i].replace(u'смиронова на', ' ')
        dataset[i] = dataset[i].replace(u'на момент осмтра ', '  ')
        dataset[i] = dataset[i].replace(u'перевод из гб ', '  ')
        dataset[i] = dataset[i].replace(u'при подъеме на ', '  ')
        dataset[i] = dataset[i].replace(u'метров ', '  ')
        dataset[i] = dataset[i].replace(u'ходьба до', ' ')
        dataset[i] = dataset[i].replace(u'однако', ' ')
        dataset[i] = dataset[i].replace(u'при остановке ', ' ')
        dataset[i] = dataset[i].replace(u' дней', '  ')
        dataset[i] = dataset[i].replace(u' имевший место', '  ')
        dataset[i] = dataset[i].replace(u' по лестнице до', '  ')
        dataset[i] = dataset[i].replace(u' эт ', '  ')
        dataset[i] = dataset[i].replace(u' -', '  ')
        dataset[i] = dataset[i].replace(u' слабость в ногах', ' слабость_в_ногах ')
        dataset[i] = dataset[i].replace(u'больного в отделении кардиологии', ' ')
        dataset[i] = dataset[i].replace(u'приняи ', ' ')
        dataset[i] = dataset[i].replace(u'при подъёме', ' ')
        dataset[i] = dataset[i].replace(u'на одышка ', 'одышка  ')
        dataset[i] = dataset[i].replace(u' около м ', '  ')
        dataset[i] = dataset[i].replace(u'при подъеме а ', ' ')
        dataset[i] = dataset[i].replace(u' отмечает ', '  ')
        dataset[i] = dataset[i].replace(u' на й ', ' ')
        dataset[i] = dataset[i].replace(u'отделении кардиологии приняли', ' ')
        dataset[i] = dataset[i].replace(u'на_момент_осмотра_жалоб_нет на_момент_осмотра_жалоб_нет',
                                                'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'боьного в', ' ')
        dataset[i] = dataset[i].replace(u'больногов', ' ')
        dataset[i] = dataset[i].replace(u'больного в', ' ')
        dataset[i] = dataset[i].replace(u'на курацию', '  ')
        dataset[i] = dataset[i].replace(u' принят ', '  ')
        dataset[i] = dataset[i].replace(u' принята ', '  ')
        dataset[i] = dataset[i].replace(u' больной ', '  ')
        dataset[i] = dataset[i].replace(u'больного ', '  ')
        dataset[i] = dataset[i].replace(u'периодически возникающий', '  ')
        dataset[i] = dataset[i].replace(u'осмотр зав отд', '  ')
        dataset[i] = dataset[i].replace(u'осмотр зав отделением', '  ')
        dataset[i] = dataset[i].replace(u'соловьёвой нв', '  ')
        dataset[i] = dataset[i].replace(u'на момент госпитализации ', '  ')
        dataset[i] = dataset[i].replace(u' месяца', '  ')
        dataset[i] = dataset[i].replace(u'чувство ', '  ')
        dataset[i] = dataset[i].replace(u' кардиологии приняли ', '  ')
        dataset[i] = dataset[i].replace(u'и ананмезом ознакомлены', ' ')
        dataset[i] = dataset[i].replace(u'жалуется на ', ' ')
        dataset[i] = dataset[i].replace(u'на момент поступления ', '  ')
        dataset[i] = dataset[i].replace(u'больницы ', '  ')
        dataset[i] = dataset[i].replace(u'активных ', '  ')
        dataset[i] = dataset[i].replace(u'совместный остмотр', ' ')
        dataset[i] = dataset[i].replace(u'смешанного характера', ' ')
        dataset[i] = dataset[i].replace(u'переведена из ко', ' ')
        dataset[i] = dataset[i].replace(u'вр морошкина нв', ' ')
        dataset[i] = dataset[i].replace(u'кривоносов дс', ' ')
        dataset[i] = dataset[i].replace(u'жалуется на', ' ')
        dataset[i] = dataset[i].replace(u'вьюковым дн', ' ')
        dataset[i] = dataset[i].replace(u'-общая_слабость ', 'общая_слабость  ')

        dataset[i] = dataset[i].replace(u'  ', '  ')

        # препараты
        dataset[i] = dataset[i].replace(u'купируются нитратами', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'эффектом от нитратов', 'купируется_нитратами ')

        dataset[i] = dataset[i].replace(u'купируемый нитратами', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'купируемый приемом нитратов', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'купирующиеся_приемом нитрато', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'купирующиеся нитропрепаратами', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'купировал нитроминтом', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'купируются после приема нитроминта', 'купируется_нитратами ')

        dataset[i] = dataset[i].replace(u'купируемый нитратами', 'купируется_нитратами ')
        # dataset[i] = dataset[i].replace(u'купирующиеся приемом', 'купирующиеся_приемом ')
        dataset[i] = dataset[i].replace(u'купируются приемом нитроглицерина', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'купируется_в_покое или нитратами',
                                                'купируется_в_покое купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'купирует нг', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u'купируются приёмом нитросорбида', 'купируется_нитратами ')
        dataset[i] = dataset[i].replace(u' или нитратами', 'купируется_нитратами ')

        dataset[i] = dataset[i].replace(u'повышенная_потливость отрицает', 'повышенную_потливость_отрицает ')

        dataset[i] = dataset[i].replace(u'на_момент_осмотра_жалоб_нет  на_момент_осмотра_жалоб_нет',
                                                'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'контакт затруднен', 'контакт_затруднен ')
        dataset[i] = dataset[i].replace(u'одышку в покое ангинозные_боли_отрицает',
                                                'одышку_в_покое_отрицает ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли перебои_в_работе_сердца кровохарканье одышку_отрицает',
                                                'ангинозные_боли_отрицает нарушение_ритма_отрицает кровохарканье_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'перебои_в_работе_сердца нарушение_ритма_отрицает',
                                                'перебои_в_работе_сердца_отрицает нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(u'чувство_нехватки_воздуха перебои_в_работе_сердца_отрицает',
                                                'чувство_нехватки_воздуха_отрицает перебои_в_работе_сердца_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли чувство_нехватки_воздуха_отрицае',
                                                'ангинозные_боли_отрицает чувство_нехватки_воздуха_отрицае ')
        dataset[i] = dataset[i].replace(u'стенокардии отрицает', 'стенокардию_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли одышка_в_покое_отрицает',
                                                'ангинозные_боли_отрицает одышка_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли одышка в покое и при_ходьбе отрицает',
                                                'ангинозные_боли_отрицает одышка_в_покое_отрицает одышка_при_ходьбе_отрицает ')
        dataset[i] = dataset[i].replace(u'боль_в_области_сердца и за грудиной отрицает',
                                                'боль_в_области_сердца_отрицает боль_за_грудиной_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли одышку кровохарканье нарушение_ритма_отрицает',
                                                'ангинозные_боли_отрицает кровохарканье_отрицает нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(u'повышенная_потливость общая_слабость отрицает',
                                                'повышенную_потливость_отрицает общая_слабость отрицает ')
        dataset[i] = dataset[i].replace(u'одышку повышенную_потливость_отрицает',
                                                'одышку_отрицает повышенную_потливость_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли одышку_отрицает',
                                                'ангинозные_боли_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли перебои_в_работе_сердца одышку_отрицает',
                                                'ангинозные_боли_отрицает перебои_в_работе_сердца_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'жалоб нет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'боль_за_грудиной одышку_отрицает',
                                                'боль_за_грудиной_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'давящие боль_за_грудиной', 'давящие_боли_за_грудиной ')
        dataset[i] = dataset[i].replace(u'давящую боль_за_грудиной', 'давящие_боли_за_грудиной ')

        dataset[i] = dataset[i].replace(u'минимальной физическая_нагрузка', 'минимальной_физической_нагрузке ')
        dataset[i] = dataset[i].replace(
            u'одышка_в_покое и при умеренной физическая_нагрузка ангинозные_боли_отрицает',
            'одышка_в_покое_отрицает ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли учащенное_сердцебиение кашель_отрицает',
                                                'ангинозные_боли_отрицает учащенное_сердцебиение_отрицает кашель_отрицает ')
        dataset[i] = dataset[i].replace(u'кашель кровохарканье подъем температуры телалихорадиты отрицает',
                                                'подъем_температуры_отрицает кашель_отрицает ')
        dataset[i] = dataset[i].replace(u'нарушение ритма синкопе_отрицает',
                                                'нарушение_ритма_отрицает синкопе_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли одышка нарушение_ритма_отрицает',
                                                'ангинозные_боли_отрицает нарушение_ритма_отрицает  ')
        dataset[i] = dataset[i].replace(
            u'перебои в области сердца синкопе повышение_артериального_давления_отрицает',
            'нарушение_ритма_отрицает , синкопе_отрицает повышение_артериального_давления_отрицает ')
        dataset[i] = dataset[i].replace(u'потери_сознания головокружений нет', 'потери_сознания головокружений нет ')
        dataset[i] = dataset[i].replace(u'учащенное_сердцебиение потери_сознания головокружение_отрицает',
                                                'учащенное_сердцебиение_отрицает потери_сознания_отрицает головокружение_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка_в_покое ангинозные_боли_отрицает',
                                                'одышка_в_покое_отрицает ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'одышка_при_ходьбе отрицает', 'одышка_при_ходьбе_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли одышка_при_ходьбе_отрицает',
                                                'ангинозные_боли_отрицает одышка_при_ходьбе_отрицает ')
        dataset[i] = dataset[i].replace(u'боль_в_области_сердца одышка_в_покое_отрицает',
                                                'боль_в_области_сердца_отрицает одышка_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные боли', 'ангинозные_боли ')
        dataset[i] = dataset[i].replace(u'ангинозный приступ', 'ангинозные_боли ')
        dataset[i] = dataset[i].replace(u'при физическая_нагрузка', 'при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'боль_за_грудиной отрицает', 'боль_за_грудиной_отрицает ')
        dataset[i] = dataset[i].replace(u'сжимающие боль_за_грудиной', 'сжатие_за_грудиной ')
        dataset[i] = dataset[i].replace(u'сжатия за грудиной', 'сжатие_за_грудиной ')
        dataset[i] = dataset[i].replace(u'одышку синкопальные состояния отрицает',
                                                'одышку_отрицает синкопальные_состояния_отрицает ')
        dataset[i] = dataset[i].replace(u'боль под левой лопаткой', 'боль_под_левой_лопаткой ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли одышку нарушение_ритма_отрицает',
                                                'ангинозные_боли_отрицает одышку_отрицает нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(
            u'ангинозные_боли одышка_в_покое и при расширени двигательного режима отрицает',
            'ангинозные_боли_отрицает одышку_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'удушья кровохаркнья отрицает', 'удушья_отрицает кровохаркнья_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли отрицает', 'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u' одышку перебои_в_работе_сердца_отрицает',
                                                ' одышку_отрицает перебои_в_работе_сердца_отрицает ')
        dataset[i] = dataset[i].replace(u' ангинозные_боли одышку_отрицает',
                                                ' ангинозные_боли_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u' одышка_в_покое и при умеренной физическая_нагрузка отрицает',
                                                ' одышка_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u' боль_за_грудиной и в левой_половине_грудной_клетки отрицает',
                                                ' боль_за_грудиной_отрицает боль_в_левой_половине_грудной_клетки отрицает ')
        dataset[i] = dataset[i].replace(u'жалоб активо нет', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'одышку при минимальной физической нагрузке',
                                                'одышка_при_физисеской_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при миним физическая_нагрузка', 'одышка_при_физисеской_нагрузке ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли одышку перебои отрицает',
                                                'ангинозные_боли_отрицает перебои_в_работе_сердца_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли синкопе_отрицает',
                                                'ангинозные_боли_отрицает синкопе_отрицает ')
        dataset[i] = dataset[i].replace(u'нарушение_ритма_сердца ангинозные_боли_отрицает',
                                                'нарушение_ритма_сердца_отрицает ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'одышку нарушение_ритма_сердца_отрицает',
                                                'одышку_отрицает нарушение_ритма_сердца_отрицает ')
        dataset[i] = dataset[i].replace(u'кашель одышку_отрицает', 'кашель_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'одышку_в_покое отрицает', 'одышку_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли_отрицает ангинозные_боли_отрицает',
                                                'ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'боль_в_области_сердца одышку_отрицает',
                                                'боль_в_области_сердца_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'боль_в_области_сердца одышку_в_покое_отрицает',
                                                'боль_в_области_сердца_отрицает одышку_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'покое одышку_отрицает', 'одышку_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли одышку_отрицает',
                                                'ангинозные_боли_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'на одышку при подъеме', 'одышка_при_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'нарушение_ритма кровохарканье_отрицает',
                                                'нарушение_ритма_отрицает кровохарканье_отрицает ')
        dataset[i] = dataset[i].replace(u'а_момент_осмотра_жалоб_нет на_момент_осмотра_жалоб_нет',
                                                'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'кровохарканье перебои_в_работе_сердца_отрицает',
                                                'кровохарканье_отрицает перебои_в_работе_сердца_отрицает ')
        dataset[i] = dataset[i].replace(u'одышку кровохарканье_отрицает', 'одышку_отрицает кровохарканье_отрицает ')
        dataset[i] = dataset[i].replace(u'на_момент_осмотра_жалоб_нет ангинозные_боли одышку_отрицает',
                                                'на_момент_осмотра_жалоб_нет ангинозные_боли_отрицает одышку_отрицает ')
        dataset[i] = dataset[i].replace(u'пресинкопе кровохарканье_отрицает',
                                                'пресинкопе_отрицает кровохарканье_отрицает ')
        dataset[i] = dataset[i].replace(u'нна_момент_осмотра_жалоб_нет', 'на_момент_осмотра_жалоб_нет ')

        # сахар

        dataset[i] = dataset[i].replace(u'повышение гликемии', 'повышение_гликемии ')
        dataset[i] = dataset[i].replace(u'повышение уровня гликемии', 'повышение_гликемии ')
        dataset[i] = dataset[i].replace(u'лабильность уровня гликемии', 'повышение_гликемии ')
        dataset[i] = dataset[i].replace(u' гипергликемия', ' повышение_гликемии ')
        dataset[i] = dataset[i].replace(u' гипергликемия', ' повышение_гликемии ')
        dataset[i] = dataset[i].replace(u' гипоргликемия', ' понижение_гликемии ')
        dataset[i] = dataset[i].replace(u' понижение гликимии', ' понижение_гликемии ')
        dataset[i] = dataset[i].replace(u' понижение уровня сахара', ' понижение_гликемии ')
        dataset[i] = dataset[i].replace(u' понижение уровня глюбкозы', 'понижение_гликемии ')

        # бщее
        dataset[i] = dataset[i].replace(u'при ходьбе', 'при_ходьбе ')
        dataset[i] = dataset[i].replace(u'на нарушение памяти', 'нарушение_памяти ')
        dataset[i] = dataset[i].replace(u'снижение памяти', 'нарушение_памяти ')
        dataset[i] = dataset[i].replace(u'умеренной физической нагрузке', 'умеренной_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'снижение слуха', 'снижение слуха ')
        dataset[i] = dataset[i].replace(u'шаткость при_ходьбе', 'шаткость_при_ходьбе ')
        dataset[i] = dataset[i].replace(u'шаткость походки', 'шаткость_при_ходьбе ')
        dataset[i] = dataset[i].replace(u'нарушение координации', 'нарушение_координации ')
        dataset[i] = dataset[i].replace(u'нарушение походки', 'шаткость_при_ходьбе ')
        dataset[i] = dataset[i].replace(u'неустойчивость при_ходьбе', 'шаткость_при_ходьбе ')
        dataset[i] = dataset[i].replace(u'купируются самостоятельно', 'купируются_в_покое ')
        dataset[i] = dataset[i].replace(u'купируется самостоятельно', 'купируются_в_покое ')
        dataset[i] = dataset[i].replace(u'проходящие самотстоятельно в покое', 'купируются_в_покое ')

        dataset[i] = dataset[i].replace(u'снижение толерантности к физическая_нагрузка',
                                                'снижение_толерантности_к_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'снижение толерантности к физ нагрузке',
                                                'снижение_толерантности_к_физической_нагрузке ')
        dataset[i] = dataset[i].replace(u'одышку при_ходьбе', 'одышка_при_ходьбе ')
        dataset[i] = dataset[i].replace(u'одышка_при_ходьбе отрицает', 'одышку_при_ходьбе_отрицает ')
        dataset[i] = dataset[i].replace(u'дискомфорт в левой_половине_грудной_клетки',
                                                'дискомфорт_в_левой_половине_грудной_клетки ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли одышку_при_ходьбе_отрицает',
                                                'ангинозные_боли_отрицает одышку_при_ходьбе_отрицает ')
        dataset[i] = dataset[i].replace(u'светлой мокроты', 'светлая_мокрота ')
        dataset[i] = dataset[i].replace(u'светлая мокрота', 'светлая_мокрота ')
        dataset[i] = dataset[i].replace(u'одышка_при_физической_нагрузке и в покое отрицает',
                                                'одышку_при_физической_нагрузке_отрицает одышку_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'вр жалоб отрицает', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'на момент осмортра отрицает', 'на_момент_осмотра_жалоб_нет ')
        dataset[i] = dataset[i].replace(u'жалоб отрицает ', 'на_момент_осмотра_жалоб_нет  ')

        dataset[i] = dataset[i].replace(u'общая_общая_слабость', ' общая_слабость ')

        dataset[i] = dataset[i].replace(u'боль в левой_половине_грудной_клетки',
                                                'боль_в_левой_половине_грудной_клетки ')

        dataset[i] = dataset[i].replace(u'головокружение отрицает', 'головокружение_отрицает ')
        dataset[i] = dataset[i].replace(u'слабость в левой руке', 'слабость_в_левой_руке ')
        dataset[i] = dataset[i].replace(u'одышку_в_покое и при_физической_нагрузке отрицает',
                                                'одышку_в_покое_отрицает одышку_при_физической_нагрузке_отрицает ')
        dataset[i] = dataset[i].replace(u'кровохарканье одышку_в_покое_отрицает',
                                                'кровохарканье_отрицает одышку_в_покое_отрицает ')
        dataset[i] = dataset[i].replace(u'типичные ангинозные_боли кровохарканье_отрицает',
                                                'ангинозные_боли_отрицает кровохарканье_отрицает ')
        dataset[i] = dataset[i].replace(
            u'ангинозные_боли одышку_в_покое и при умеренных физических нагрузках перебои_в_работе_сердца_отрицает',
            'ангинозные_боли_отрицает одышку_в_покое_отрицает одышку_при_физическиз_нагрузках_отрицает перебои_в_работе_сердца_отрицает ')

        dataset[i] = dataset[i].replace(u'т д глебовской', ' ')
        dataset[i] = dataset[i].replace(u'__волошиновой_а п', ' ')
        dataset[i] = dataset[i].replace(u'соловьёвой н в н а ', ' ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли нарушение_ритма_отрицает',
                                                'ангинозные_боли_отрицает нарушение_ритма_отрицает ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли перебои_в_работе_сердца синкопе пресинкопе_отрицает',
                                                'ангинозные_боли_отрицает перебои_в_работе_сердца_отрицает синкопе_отрицает пресинкопе_отрицает ')
        dataset[i] = dataset[i].replace(u'одышку ангинозные_боли_отрицает',
                                                'одышку_отрицает ангинозные_боли_отрицает ')
        dataset[i] = dataset[i].replace(u'одышкой ', 'одышка  ')
        dataset[i] = dataset[i].replace(u'одышку ', 'одышка  ')

        dataset[i] = dataset[i].replace(u'одышку_в_покое и при умеренной ф н отрицает',
                                                'одышку_в_поко_отрицает одышку_при_физической_нагрузке_отрицает ')

        dataset[i] = dataset[i].replace(u'соловьёвой н а н а ', ' ')

        dataset[i] = dataset[i].replace(u'с з о зуевой и б', ' ')
        dataset[i] = dataset[i].replace(u'к о княжевская е а вр з о', ' ')
        dataset[i] = dataset[i].replace(u'жалоб ', ' ')
        dataset[i] = dataset[i].replace(u'боль в прекардиальной области', 'боль_в_области_сердца ')
        dataset[i] = dataset[i].replace(u'ангинозные_боли_за_грудиной', ' ангинозные_боли ')

        dataset[i] = dataset[i].replace(u' повышение ад отрицает', ' повышение_ад_отрицает ')
        dataset[i] = dataset[i].replace(u' хронические заболевания отрицает', ' хронические_заболевания_отрицает ')
        dataset[i] = dataset[i].replace(u' гинекологический анамнез', ' гинекологический_анамнез ')
        dataset[i] = dataset[i].replace(u' регулярные необильные', ' регулярные_необильные ')
        dataset[i] = dataset[i].replace(u'регулярные необильные', ' регулярные_необильные ')

        dataset[i] = dataset[i].replace(u' аллергия на', ' аллергия_на ')
        dataset[i] = dataset[i].replace(u'гинекологический анамнез ', ' гинекологический_анамнез ')
        dataset[i] = dataset[i].replace(u' регулярные обильные ',  ' регулярные_обильные ')
        dataset[i] = dataset[i].replace(u'регулярные обильные ',  ' регулярные_обильные ')
        dataset[i] = dataset[i].replace(u' аллергии отрицает ',  ' аллергию_отрицает ')



        print(i, " of ", len(dataset), " ",dataset[i])




    toc = time()
    # print(" Time ", toc - tic)
    return dataset

def morph_processing(dataset):
    morph = MorphAnalyzer()
    for i in range(0, len(dataset)):
        #dataset[i] = dataset[i].lower()
        #dataset[i] = re.sub(r'<[^>]+>', ' ', dataset[i])
        #dataset[i] = re.sub(r'[^а-я ]+', ' ', dataset[i])
        dataset[i] = re.sub(r' +', ' ', dataset[i])
        words = dataset[i].split('  ')
        new_line = []
        for word in words:
            if len(word) > 2:
                word = morph.parse(word)[0]
                if word.tag.POS not in ['PREP', 'NUMR', 'CONJ', 'PRCL', 'PRED', 'NPRO']:
                    new_line.append(word.normal_form)
        if len(new_line) > 0:
            dataset[i] = (' '.join(new_line))
        else:
            dataset[i] = ''
    return dataset
