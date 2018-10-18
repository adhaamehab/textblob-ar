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
    >>> text = """ في أنظمة التشغيل متعددة المهام مثل اليونكس عفريت النظام هو برنامج يعمل في خلفية النظام بعيدا عن التحكم المباشر من المستحدم وغالبا ما يبدأ عمله كعملية خلفية مع بداية تشغيل النظام."""
    >>> blob = TextBlob(text)
    >>> print(blob.tags)
    [('', 'في/IN'), ('', 'أنظمة/NN'), ('', 'التشغيل/DTNN'), ('', 'متعددة/JJ'), ('', 'المهام/DTNN'), ('', 'مثل/NN'), ('', 'اليونكس/DTNNP'), ('', 'عفريت/NNP'), ('', 'النظام/DTNN'), ('', 'هو/PRP'), ('', 'برنامج/NN'), ('', 'يعمل/VBP'), ('', 'في/IN'), ('', 'خلفية/NN'), ('', 'النظام/DTNN'), ('', 'بعيدا/JJ'), ('', 'عن/IN'), ('', 'التحكم/DTNN'), ('', 'المباشر/DTJJ'), ('', 'من/IN'), ('', 'المستحدم/DTNN'), ('', 'وغالبا/NN'), ('', 'ما/WP'), ('', 'يبدأ/VBP'), ('', 'عمله/NN'), ('', 'كعملية/JJ'), ('', 'خلفية/NN'), ('', 'مع/NN'), ('', 'بداية/NN'), ('', 'تشغيل/NN'), ('', 'النظام/DTNN')]

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