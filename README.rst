===========
textblob-ar [WIP]
===========

Arabic language support for `TextBlob`_.

Features
--------

* Tokenizer
* Supports Python 2 and 3


Usage
-----
.. code-block:: python

    >>> from textblob_ar import TextBlobAR as TextBlob
    >>> blob = TextBlob(u"""هندسة البرمجيات هي دراسة تصميم وتنفيذ وتعديل البرمجيات بما يضمن توفر هذه البرمجيات بجودة عالية وتكلفة معقولة متاحة للجميع وقابلة للتطوير فيما بعد وسريعة للبناء. وهندسة البرمجيات تقوم على أسس ونظريات من الهندسة وعلوم الحاسب كمبدأ ال Functional Structure من الهندسة والذي يعتمد على مبدأ تصميم أجزاء صغيرة تتجانس في العمل مع بعضها لتشكل عمل الكل.""")
    >>> blob.tokens
    WordList(['هندسة', 'البرمجيات', 'هي', 'دراسة', 'تصميم', 'وتنفيذ', 'وتعديل', 'البرمجيات', 'بما', 'يضمن', 'توفر', 'هذه', 'البرمجيات', 'بجودة', 'عالية', 'وتكلفة', 'معقولة', 'متاحة', 'للجميع', 'وقابلة', 'للتطوير', 'فيما', 'بعد', 'وسريعة', 'للبناء', '.', 'وهندسة', 'البرمجيات', 'تقوم', 'على', 'أسس', 'ونظريات', 'من', 'الهندسة', 'وعلوم', 'الحاسب', 'كمبدأ', 'ال', 'Functional', 'Structure', 'من', 'الهندسة', 'والذي', 'يعتمد', 'على', 'مبدأ', 'تصميم', 'أجزاء', 'صغيرة', 'تتجانس', 'في', 'العمل', 'مع', 'بعضها', 'لتشكل', 'عمل', 'الكل', '.'])

Requirements
------------

- Python >= 2.6 or >= 3.5

TODO
----

- POS
- Correction
- Sentiment
- Grammer
License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/textblob-fr/blob/master/LICENSE>`_ file for more details.

.. _TextBlob: https://textblob.readthedocs.org/