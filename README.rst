===========
textblob-ar [WIP]
===========

.. image:: https://travis-ci.org/adhaamehab/textblob-ar.svg?branch=master
    :target: https://travis-ci.org/adhaamehab/textblob-ar

Arabic language support for `TextBlob`_.

Features
--------

* Tokenizer
* Sentiment analysis
* Stanford Arabic POS


Usage
-----

**Tokenizer**
  
.. code-block:: python

    >>> from textblob_ar import TextBlob
    >>> blob = TextBlob(u"""هندسة البرمجيات هي دراسة تصميم وتنفيذ وتعديل البرمجيات بما يضمن توفر هذه البرمجيات بجودة عالية وتكلفة معقولة متاحة للجميع وقابلة للتطوير فيما بعد وسريعة للبناء. وهندسة البرمجيات تقوم على أسس ونظريات من الهندسة وعلوم الحاسب كمبدأ ال Functional Structure من الهندسة والذي يعتمد على مبدأ تصميم أجزاء صغيرة تتجانس في العمل مع بعضها لتشكل عمل الكل.""")
    >>> blob.tokens
    WordList(['هندسة', 'البرمجيات', 'هي', 'دراسة', 'تصميم', 'وتنفيذ', 'وتعديل', 'البرمجيات', 'بما', 'يضمن', 'توفر', 'هذه', 'البرمجيات', 'بجودة', 'عالية', 'وتكلفة', 'معقولة', 'متاحة', 'للجميع', 'وقابلة', 'للتطوير', 'فيما', 'بعد', 'وسريعة', 'للبناء', '.', 'وهندسة', 'البرمجيات', 'تقوم', 'على', 'أسس', 'ونظريات', 'من', 'الهندسة', 'وعلوم', 'الحاسب', 'كمبدأ', 'ال', 'Functional', 'Structure', 'من', 'الهندسة', 'والذي', 'يعتمد', 'على', 'مبدأ', 'تصميم', 'أجزاء', 'صغيرة', 'تتجانس', 'في', 'العمل', 'مع', 'بعضها', 'لتشكل', 'عمل', 'الكل', '.'])


**Sentiment**

.. code-block:: python

    >>> from textblob_ar import TextBlob
    >>> blob = TextBlob('اعجبني هذا الكتاب. اعترض قليلا مع بعض افكاره لكن مضمونه رائع')
    >>> blob.sentiment
    Sentiment(polarity=0.8, subjectivity=0.9)
    >>> blob = TextBlob('لم يعجبني هذا الكتاب. مضمونه سئ')
    >>> blob.sentiment
    Sentiment(polarity=-0.6999999999999998, subjectivity=0.6666666666666666)


**Stanford POS**

Note that Stanford POS is the defualt one untill the main one is released
.. code-block:: python

    >>> from textblob_ar import TextBlob
    >>> text = """ حرب أكتوبر "حرب العاشر من رمضان" كما تعرف في مصر أو حرب تشرين التحريرية كما تعرف في سوريا
 أو حرب يوم الغفران (بالعبرية: מלחמת יום כיפור، ميلخمت يوم كيبور)
 كما تعرف في إسرائيل، هي ح رب شنتها كل من مصر وسوريا على إسرائيل عام 
1973 وهي رابع الحروب العربية الإسرائيلية بعد حرب 1948 (حرب فلسطين)،
 وحرب 1956 (حرب السويس) وحرب 1967 (حرب الستة أيام)، وكانت إسرائيل في الحرب
 الثالثة قد احتلت شبه جزيرة سيناء من مصر
  وهضبة الجولان من سوريا إلى جانب الضفة الغربية من الأردن
   بالإضافة إلى قطاع غزة الخاضع آنذاك لحكم عسكري مصري.
  بدأت الحرب يوم السبت 6 أكتوبر/ تشرين الأول 1
    973 م الموافق 10 رمضان 1393 هـ بتنسيق هجومين مفاجئين ومتزامنين على القوات الإسرائيلية؛
     أحدهما للجيش المصري على جبهة سيناء المحتلة 
     وآخر للجيش السوري على جبهة هضبة الجولان المحتلة. وساهم في
    الحرب بعض الدول العربية سواء بالدعم العسكري أو الاقتصادي."""
    >>> blob = TextBlob(text)
    >>> print(blob.tags)

Requirements
------------

- Python >= 3.3

TODO
----

- Part Of Speech tagger
- Noun-phrases extraction
- Parser
- Classification support
- Correction
- Grammer


License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/textblob-fr/blob/master/LICENSE>`_ file for more details.

.. _TextBlob: https://textblob.readthedocs.org/