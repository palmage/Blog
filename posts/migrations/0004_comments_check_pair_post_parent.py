# Generated by Django 3.2.8 on 2021-10-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211027_2343'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='comments',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('post', None), models.Q(('parent', None), _negated=True)), models.Q(models.Q(('post', None), _negated=True), ('parent', None)), _connector='OR'), name='check_pair_post_parent'),
        ),
    ]
