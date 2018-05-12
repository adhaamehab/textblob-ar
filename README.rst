===========
textblob-ar [WIP]
===========

Arabic language support for `TextBlob`_.

Features
--------

* Tokenizer
* Sentiment analysis


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

Requirements
------------

- Python >= 3.3

TODO
----

- POS
- Parser
- Classification support
- Correction
- Grammer


License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/textblob-fr/blob/master/LICENSE>`_ file for more details.

.. _TextBlob: https://textblob.readthedocs.org/