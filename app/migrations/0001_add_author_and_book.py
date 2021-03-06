# Generated by Django 2.1.1 on 2018-09-12 20:47

from django.db import migrations, models
from django.core.files.images import ImageFile

books = [
    {
        'title':
            'F# Deep Dives',
        'authors': ['Tomas Petricek', 'Philip Trelford'],
        'price_cents':
            3256,
        'img_path':
            'fsharp_deep_dives.png',
        'description': (
            'F# Deep Dives presents a collection of real-world F# techniques, each written by expert practitioners. '
            'Each chapter presents a new use case where you\'ll read how the author used F# to solve a complex problem '
            'more effectively than would have been possible using a traditional approach. You\'ll not only see how a '
            'specific solution works in a specific domain, you\'ll also learn how F# developers approach problems, what '
            'concepts they use to solve them, and how they integrate F# into existing systems and environments.'
        )
    },
    {
        'title':
            'Get Programming with F#',
        'authors': ['Isaac Abraham'],
        'price_cents':
            3599,
        'img_path':
            'get_programming_with_fsharp.png',
        'description': (
            'Get Programming with F#: A guide for .NET Developers shows you how to upgrade your .NET development skills '
            'by adding a touch of functional programming in F#. In just 43 bite-size chunks, you\'ll learn to use F# to '
            'tackle the most common .NET programming tasks. You\'ll start with the basics of F# and functional programming, '
            'building on your existing skills in the .NET framework. Examples use the familiar Visual Studio environment, '
            'so you\'ll be instantly comfortable. Packed with enlightening examples, real-world use cases, and plenty of '
            'easy-to-digest code, this easy-to-follow tutorial will make you wonder why you didn\'t pick up F# years ago!'
        )
    },
    {
        'title':
            'Real World Functional Programming',
        'authors': ['Tomas Petricek', 'Jon Skeet'],
        'price_cents':
            3999,
        'img_path':
            'real_world_functional_programming.png',
        'description': (
            'This book teaches the ideas and techniques of functional programming applied to real-world problems. You\'ll '
            'see how the functional way of thinking changes the game for .NET developers. Then, you\'ll tackle common '
            'issues using a functional approach. The book will also teach you the basics of the F# language and extend '
            'your C# skills into the functional domain. No prior experience with functional programming or F# is required.'
        )
    },
    {
        'title':
            'Scala in Action',
        'authors': ['Nilanjan Raychaudhuri'],
        'price_cents':
            3599,
        'img_path':
            'scala_in_action.png',
        'description': (
            'Scala in Action is a comprehensive tutorial that introduces Scala through clear explanations and numerous hands-on '
            'examples. Because Scala is a rich and deep language, it can be daunting to absorb all the new concepts at once. '
            'This book takes a "how-to" approach, explaining language concepts as you explore familiar programming '
            'challenges that you face in your day-to-day work.')
    },
    {
        'title':
            'Scala in Depth',
        'authors': ['Joshua D. Suereth'],
        'price_cents':
            3599,
        'img_path':
            'scala_in_depth.png',
        'description': (
            'Scala in Depth is a unique new book designed to help you integrate Scala effectively into your '
            'development process. By presenting the emerging best practices and designs from the Scala '
            'community, it guides you through dozens of powerful techniques example by example.')
    },
    {
        'title':
            'Functional Programming in Scala',
        'authors': ['Paul Chiusano', 'Runar Bjarnason'],
        'price_cents':
            3599,
        'img_path':
            'functional_programming_in_scala.png',
        'description': (
            'Functional Programming in Scala is a serious tutorial for programmers looking to learn FP and '
            'apply it to the everyday business of coding. The book guides readers from basic techniques to '
            'advanced topics in a logical, concise, and clear progression. In it, you\'ll find concrete '
            'examples and exercises that open up the world of functional programming.')
    },
    {
        'title':
            'The Joy of Clojure',
        'authors': ['Michael Fogus', 'Chris Houser'],
        'price_cents':
            3999,
        'img_path':
            'the_joy_of_clojure.png',
        'description': (
            'The Joy of Clojure, Second Edition is a deep account of the Clojure language. Fully updated '
            'for Clojure 1.6, this new edition goes beyond the syntax to show you how to write fluent Clojure '
            'code. You\'ll learn functional and declarative approaches to programming and will master techniques '
            'that make Clojure elegant and efficient. The book shows you how to solve hard problems related '
            'to concurrency, interoperability, and performance, and how great it can be to think in the Clojure way.'
        )
    },
    {
        'title':
            'Clojure in Action',
        'authors': ['Amit Rathore', 'Francis Avila'],
        'price_cents':
            3999,
        'img_path':
            'clojure_in_action.png',
        'description': (
            'Clojure in Action, Second Edition is an expanded and improved version that?s been updated to cover '
            'the new features of Clojure 1.6. The book gives you a rapid introduction to the Clojure language, '
            'moving from abstract theory to practical examples. You\'ll start by learning how to use Clojure as '
            'a general-purpose language. Next, you\'ll explore Clojure\'s efficient concurrency model, based on '
            'the database concept of Software Transactional Memory (STM). You\'ll gain a new level of '
            'productivity through Clojure DSLs that can run on the JVM. Along the way, you\'ll learn countless '
            'tips, tricks, and techniques for writing smaller, safer, and faster code.')
    },
    {
        'title':
            'Get Programming With Haskell',
        'authors': ['Will Kurt'],
        'price_cents':
            3599,
        'img_path':
            'get_programming_with_haskell.png',
        'description': (
            'Get Programming with Haskell introduces you to the Haskell language without drowning you in '
            'academic jargon and heavy functional programming theory. By working through 43 easy-to-follow '
            'lessons, you\'ll learn Haskell by doing Haskell. This book starts with first concepts, building '
            'your knowledge with concrete examples and exercises. You\'ll learn to think the Haskell way, as '
            'you start to understand the language and how to use it effectively. And you\'ll really appreciate '
            'the crystal-clear illustrations, quick-checks, and open-ended tasks that make sure you\'re solid '
            'on each new concept before you move along!')
    },
]


def add_initial_books_and_authors(apps, _schema_editor):
    Book = apps.get_model('app', 'Book')
    Author = apps.get_model('app', 'Author')

    for book_data in books:
        author_names = book_data.pop('authors')
        img_path = book_data.pop('img_path')
        price = book_data.pop('price_cents') / 100
        book = Book.objects.create(
            cover_image=ImageFile(open('initial_book_images/' + img_path, 'rb'), name=img_path),
            price=price,
            **book_data)
        for name in author_names:
            author, _created = Author.objects.get_or_create(name=name)
            book.authors.add(author)


def do_nothing(_apps, _schema_editor):
    pass


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'default_related_name': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('price', models.FloatField()),
                ('cover_image', models.ImageField(upload_to='book_covers')),
                ('description', models.TextField()),
                ('authors', models.ManyToManyField(related_name='books', to='app.Author')),
            ],
            options={
                'default_related_name': 'books',
            },
        ),
        migrations.RunPython(add_initial_books_and_authors, reverse_code=do_nothing),
    ]
