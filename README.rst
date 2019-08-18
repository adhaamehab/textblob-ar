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
* Spelling Correction
* Text similarity
* Fasttext arabic word2vec interface

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
    >>> from textblob_ar.pos_tagger import StanfordPOSTagger
    >>> tagg = StanfordPOSTagger()
    >>> text = """ في أنظمة التشغيل متعددة المهام مثل اليونكس عفريت النظام هو برنامج يعمل في خلفية النظام بعيدا عن التحكم المباشر من المستحدم وغالبا ما يبدأ عمله كعملية خلفية مع بداية تشغيل النظام."""
    >>> blob = TextBlob(text, pos_tagger=tagger)
    >>> print(blob.tags)
    [('', 'في/IN'), ('', 'أنظمة/NN'), ('', 'التشغيل/DTNN'), ('', 'متعددة/JJ'), ('', 'المهام/DTNN'), ('', 'مثل/NN'), ('', 'اليونكس/DTNNP'), ('', 'عفريت/NNP'), ('', 'النظام/DTNN'), ('', 'هو/PRP'), ('', 'برنامج/NN'), ('', 'يعمل/VBP'), ('', 'في/IN'), ('', 'خلفية/NN'), ('', 'النظام/DTNN'), ('', 'بعيدا/JJ'), ('', 'عن/IN'), ('', 'التحكم/DTNN'), ('', 'المباشر/DTJJ'), ('', 'من/IN'), ('', 'المستحدم/DTNN'), ('', 'وغالبا/NN'), ('', 'ما/WP'), ('', 'يبدأ/VBP'), ('', 'عمله/NN'), ('', 'كعملية/JJ'), ('', 'خلفية/NN'), ('', 'مع/NN'), ('', 'بداية/NN'), ('', 'تشغيل/NN'), ('', 'النظام/DTNN')]


**Text Correction**

Thanks for `Peter Norvig http://norvig.com/spell-correct.html`

.. code-block:: python

    >>> from textblob_ar import TextBlob
    >>> from textblob_ar.correction import TextCorrection
    >>> text = 'الاذدهاز'
    >>> TextCorrection().correct(text)
    {'الاذهان', 'الازدهار', 'الادهان', 'الاندهاش'}
    >>> TextCorrection().correct(text, top=True)
    'الازدهاز'

**Text Similarity**

Based on `gensim <https://radimrehurek.com/gensim>`_ and `Fasttext <https://fasttext.cc/docs/en/pretrained-vectors.html>`_  pretrained word2vec model 

The procedure used in calculating similarity
is calculating mean feature vector for each sentence.
Then calculate the cosine distance between those two vectors.


.. code-block:: python

    >>> from textblob_ar import TextSimilarity
    >>> sim = TextSimilarity()
    # takes around 12 second (macbook pro 2017) to load the pretrained word2vec
    >>> sent1 = u'الإرهابي الصالح هي رواية خيال سياسي للكاتبة دوريس ليسينج. ظهرت أول طبعة للرواية في سبتمبر من عام 1985 للناشرين جوناثان كيب في المملكة المتحدة وألفريد أ'
    >>> sent2 = u'روايه الكاتبه دوريس ليسينج هي روايه خيال سياسي ظهرت في سبتمبر 1985 بعنوان الارهابي الصالح وتم نشرها عن طريق جوناثان كيب والفريد أ في انجلترا'
    >>> sim.similarity(sent1, sent2)
    0.9611366391181946


Requirements
------------

- Python >= 3.3

Installation
------------
* Development

.. code-block:: shell
    $ git clone https://github.com/adhaamehab/textblob-ar.git
    $ cd textblob_ar
    $ virtualenv -p python3 env
    $ source env/bin/activate
    $ pip install -Ur dev-requirements.txt

for text similarity download fasttext arabic word2vec pretrained model from  `here <https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md>`_


TODO
----

- Part Of Speech tagger
- Noun-phrases extraction
- Parser
- Classification support
- Grammer


License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/textblob-fr/blob/master/LICENSE>`_ file for more details.

.. _TextBlob: https://textblob.readthedocs.org/


.. image:: https://badges.gitter.im/textblob-ar/community.svg
   :alt: Join the chat at https://gitter.im/textblob-ar/community
   :target: https://gitter.im/textblob-ar/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
