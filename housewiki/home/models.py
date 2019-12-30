"""
…/HouseWiki/housewiki/home/models.py
"""


from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
# from django.db


# def get_absolute_url(list_name):
    # return reverse(f'housewiki:')


# each attribute in each defined class will have a table
# created for it by Django in the DB


class Property(models.Model):

    PROPERTY_RANKING_CHOICES = (('current favorite (1)',
                                 'Current favorite (1)'),
                                ('backup favorite (1.5)',
                                 'Backup favorite (1.5)'),
                                ('really like it (2)',
                                 'Really like it (2)'),
                                ('like it (3)',
                                 'Like it (3)'),
                                ('acceptable, but least favorite (4)',
                                 'Acceptable, but least favorite (4)'))

    ROOM_COUNT = (('1', '1'), ('2', '2'), ('3', '3'),
                  ('4', '4'), ('5 and up', '5 & up'))
    BATH_COUNT = (('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'),
                  ('3', '3'), ('3.5', '3.5'),
                  ('4', '4'), ('4.5', '4.5'),
                  ('5 and up', '5 & up'))
    GARAGE_CAR_COUNT = (('1 car', '1 car'),
                        ('1 car with nook', '1 car with nook'),
                        ('2 car', '2 car'),
                        ('2 car with nook', '2 car with nook'),
                        ('3 car', '3 car'),
                        ('3 car with nook', '3 car with nook'))
    # oh, yes, I _do_ hate myself, why do you ask?
    HOUSE_PRICES = (('$ 190 k', '$ 190 k'), ('$ 191 k', '$ 191 k'), ('$ 192 k', '$ 192 k'), ('$ 193 k', '$ 193 k'), ('$ 194 k', '$ 194 k'), ('$ 195 k', '$ 195 k'), ('$ 196 k', '$ 196 k'), ('$ 197 k', '$ 197 k'), ('$ 198 k', '$ 198 k'), ('$ 199 k', '$ 199 k'),
                    ('$ 200 k', '$ 200 k'), ('$ 201 k', '$ 201 k'), ('$ 202 k', '$ 202 k'), ('$ 203 k', '$ 203 k'), ('$ 204 k', '$ 204 k'), ('$ 205 k', '$ 205 k'), ('$ 206 k', '$ 206 k'), ('$ 207 k', '$ 207 k'), ('$ 208 k', '$ 208 k'), ('$ 209 k', '$ 209 k'),
                    ('$ 210 k', '$ 210 k'), ('$ 211 k', '$ 211 k'), ('$ 212 k', '$ 212 k'), ('$ 213 k', '$ 213 k'), ('$ 214 k', '$ 214 k'), ('$ 215 k', '$ 215 k'), ('$ 216 k', '$ 216 k'), ('$ 217 k', '$ 217 k'), ('$ 218 k', '$ 218 k'), ('$ 219 k', '$ 219 k'),
                    ('$ 220 k', '$ 220 k'), ('$ 221 k', '$ 221 k'), ('$ 222 k', '$ 222 k'), ('$ 223 k', '$ 223 k'), ('$ 224 k', '$ 224 k'), ('$ 225 k', '$ 225 k'), ('$ 226 k', '$ 226 k'), ('$ 227 k', '$ 227 k'), ('$ 228 k', '$ 228 k'), ('$ 229 k', '$ 229 k'),
                    ('$ 230 k', '$ 230 k'), ('$ 231 k', '$ 231 k'), ('$ 232 k', '$ 232 k'), ('$ 233 k', '$ 233 k'), ('$ 234 k', '$ 234 k'), ('$ 235 k', '$ 235 k'), ('$ 236 k', '$ 236 k'), ('$ 237 k', '$ 237 k'), ('$ 238 k', '$ 238 k'), ('$ 239 k', '$ 239 k'),
                    ('$ 240 k', '$ 240 k'), ('$ 241 k', '$ 241 k'), ('$ 242 k', '$ 242 k'), ('$ 243 k', '$ 243 k'), ('$ 244 k', '$ 244 k'), ('$ 245 k', '$ 245 k'), ('$ 246 k', '$ 246 k'), ('$ 247 k', '$ 247 k'), ('$ 248 k', '$ 248 k'), ('$ 249 k', '$ 249 k'),
                    ('$ 250 k', '$ 250 k'), ('$ 251 k', '$ 251 k'), ('$ 252 k', '$ 252 k'), ('$ 253 k', '$ 253 k'), ('$ 254 k', '$ 254 k'), ('$ 255 k', '$ 255 k'), ('$ 256 k', '$ 256 k'), ('$ 257 k', '$ 257 k'), ('$ 258 k', '$ 258 k'), ('$ 259 k', '$ 259 k'),
                    ('$ 260 k', '$ 260 k'), ('$ 261 k', '$ 261 k'), ('$ 262 k', '$ 262 k'), ('$ 263 k', '$ 263 k'), ('$ 264 k', '$ 264 k'), ('$ 265 k', '$ 265 k'), ('$ 266 k', '$ 266 k'), ('$ 267 k', '$ 267 k'), ('$ 268 k', '$ 268 k'), ('$ 269 k', '$ 269 k'),
                    ('$ 270 k', '$ 270 k'), ('$ 271 k', '$ 271 k'), ('$ 272 k', '$ 272 k'), ('$ 273 k', '$ 273 k'), ('$ 274 k', '$ 274 k'), ('$ 275 k', '$ 275 k'), ('$ 276 k', '$ 276 k'), ('$ 277 k', '$ 277 k'), ('$ 278 k', '$ 278 k'), ('$ 279 k', '$ 279 k'),
                    ('$ 280 k', '$ 280 k'), ('$ 281 k', '$ 281 k'), ('$ 282 k', '$ 282 k'), ('$ 283 k', '$ 283 k'), ('$ 284 k', '$ 284 k'), ('$ 285 k', '$ 285 k'), ('$ 286 k', '$ 286 k'), ('$ 287 k', '$ 287 k'), ('$ 288 k', '$ 288 k'), ('$ 289 k', '$ 289 k'),
                    ('$ 290 k', '$ 290 k'), ('$ 291 k', '$ 291 k'), ('$ 292 k', '$ 292 k'), ('$ 293 k', '$ 293 k'), ('$ 294 k', '$ 294 k'), ('$ 295 k', '$ 295 k'), ('$ 296 k', '$ 296 k'), ('$ 297 k', '$ 297 k'), ('$ 298 k', '$ 298 k'), ('$ 299 k', '$ 299 k'),
                    ('$ 300 k', '$ 300 k'), ('$ 301 k', '$ 301 k'), ('$ 302 k', '$ 302 k'), ('$ 303 k', '$ 303 k'), ('$ 304 k', '$ 304 k'), ('$ 305 k', '$ 305 k'), ('$ 306 k', '$ 306 k'), ('$ 307 k', '$ 307 k'), ('$ 308 k', '$ 308 k'), ('$ 309 k', '$ 309 k'))

    floorplan_name = models.CharField(max_length=100)
    community_name = models.CharField(max_length=100)
    builder_name = models.CharField(max_length=100)
    # sum of all three fields dictates this length
    # see definition of 'save' in this class for usage
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)
    cover = models.ImageField(upload_to='images/')

    floorplan_link = models.URLField()
    ranking = models.CharField(max_length=40,
                               choices=PROPERTY_RANKING_CHOICES,
                               default='really like it (2)')
    square_footage = models.IntegerField()
    bedrooms = models.CharField(max_length=10,
                                choices=ROOM_COUNT,
                                default='1')

    bathrooms = models.CharField(max_length=10,
                                 choices=BATH_COUNT,
                                 default='1')

    garage = models.CharField(max_length=20,
                              choices=GARAGE_CAR_COUNT,
                              default='1 car')

    optional_floorplan_info = models.TextField(null=True, blank=True)

    standout_features = models.TextField(null=True, blank=True)
    desired_options = models.TextField(null=True, blank=True)

    rounded_total_price = models.CharField(max_length=8,
                                           choices=HOUSE_PRICES,
                                           default='$ 190 k')


    # class_string = ', '.join((f'{floorplan_name}',
    #                           f'{community_name}',
    #                           f'{builder_name}'))
    def class_string(self):
        return ', '.join((f'{self.floorplan_name}',
                          f'{self.community_name}',
                          f'{self.builder_name}'))

    string_property = property(class_string)


    def save(self, *args, **kwargs):
        # check if floorplan community or builder names changed
        self.slug = '-'.join((slugify(self.builder_name),
                                       slugify(self.community_name),
                                       slugify(self.floorplan_name)))
        super(Property, self).save(*args, **kwargs)


    class Meta:
        ordering = ('ranking',)


    def __str__(self):
        return self.class_string()



class Milestone(models.Model):

    MILESTONE_STATUS_CHOICES = (('reached', 'Reached'),
                                ('not reached', 'Not Reached'))

    # to be used as title, VARCHAR in DB
    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250,
                            ##unique_for_date='Reached'
                            unique=True)

    # create a foreign key in DB using primary key of User
    creator = models.ForeignKey(User,
                                # required but also SQL standard
                                # delete Milestones on user delete
                                on_delete=models.CASCADE,
                                # the reverse relationship
                                # from User to milestone
                                related_name='milestones')

    comment = models.TextField(null=True,
                               blank=True)

    ##reached_date = models.DateTimeField(default=timezone.now)

    # saves the date automatically when creating an object
    created = models.DateTimeField(auto_now_add=True)

    # saves the date automatically when saving an object
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=20,
                              choices=MILESTONE_STATUS_CHOICES,
                              default='not reached')

    ##reached = models.BooleanField(default=False)

    class Meta:
        # recent to oldest when querying DB
        ordering = ('-created',)

    # human readable representation of this object
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('housewiki:')



class Question(models.Model):

    QUESTION_STATUS_CHOICES = (('answered', 'Answered'),
                               ('unanswered', 'Unanswered'))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    supplemental_example = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('answered',)

    def __str__(self):
        return self.title



class WishList(models.Model):

    WISH_RANKING_CHOICES = (('dealbreaker (1)', 'Dealbreaker (1)'),
                            ('very important (2)', 'Very Important (2)'),
                            ('important (3)', 'Important (3)'),
                            ('kind of important (4)', 'Kind of Important (4)'),
                            ('almost petty (5)', 'Almost Petty (5)'),
                            ('definitely petty (6)', 'Definitely Petty (6)'))

    wish = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    ranking = models.CharField(max_length=25,
                               choices=WISH_RANKING_CHOICES,
                               default='kind of important (4)')

    class Meta:
        ordering = ('ranking',)

    def __str__(self):
        return self.wish


class KnowledgeAndTips(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class ThingsToConsider(models.Model):

    CONSIDERED_RANKING_CHOICES = (('high importance (1)', 'High Importance (1)'),
                                  ('medium importance (2)', 'Medium Importance (2)'),
                                  ('low importance (3)', 'Low Importance (3)'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    ranking = models.CharField(max_length=25,
                               choices=CONSIDERED_RANKING_CHOICES,
                               default='medium importance (2)')

    class Meta:
        ordering = ('ranking',)

    def __str__(self):
        return self.title



