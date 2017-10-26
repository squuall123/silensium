# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-16 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_auto_20160906_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Rest of World'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('WF', 'Wallis and Futuna'), ('BL', 'Saint Barth\xe9lemy'), ('BM', 'Bermuda'), ('BN', 'Brunei'), ('BO', 'Bolivia'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BT', 'Bhutan'), ('JM', 'Jamaica'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('WS', 'Samoa'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BR', 'Brazil'), ('BS', 'Bahamas'), ('JE', 'Jersey'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('RS', 'Serbia'), ('TL', 'Timor-Leste'), ('RE', 'R\xe9union'), ('TM', 'Turkmenistan'), ('TJ', 'Tajikistan'), ('RO', 'Romania'), ('TK', 'Tokelau'), ('GW', 'Guinea-Bissau'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GR', 'Greece'), ('GQ', 'Equatorial Guinea'), ('GP', 'Guadeloupe'), ('JP', 'Japan'), ('GY', 'Guyana'), ('GG', 'Guernsey'), ('GF', 'French Guiana'), ('GE', 'Georgia'), ('GD', 'Grenada'), ('GB', 'United Kingdom'), ('GA', 'Gabon'), ('GN', 'Guinea'), ('GM', 'Gambia'), ('GL', 'Greenland'), ('GI', 'Gibraltar'), ('GH', 'Ghana'), ('OM', 'Oman'), ('TN', 'Tunisia'), ('JO', 'Jordan'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('HK', 'Hong Kong'), ('HN', 'Honduras'), ('HM', 'Heard Island and McDonald Islands'), ('VE', 'Venezuela'), ('PR', 'Puerto Rico'), ('PS', 'Palestine, State of'), ('PW', 'Palau'), ('PT', 'Portugal'), ('KN', 'Saint Kitts and Nevis'), ('PY', 'Paraguay'), ('IQ', 'Iraq'), ('PA', 'Panama'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PE', 'Peru'), ('PK', 'Pakistan'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PM', 'Saint Pierre and Miquelon'), ('ZM', 'Zambia'), ('EH', 'Western Sahara'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('ZA', 'South Africa'), ('EC', 'Ecuador'), ('IT', 'Italy'), ('VN', 'Vietnam'), ('SB', 'Solomon Islands'), ('ET', 'Ethiopia'), ('SO', 'Somalia'), ('ZW', 'Zimbabwe'), ('SA', 'Saudi Arabia'), ('ES', 'Spain'), ('ER', 'Eritrea'), ('ME', 'Montenegro'), ('MD', 'Moldova'), ('MG', 'Madagascar'), ('MF', 'Saint Martin (French part)'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('UZ', 'Uzbekistan'), ('MM', 'Myanmar'), ('ML', 'Mali'), ('MO', 'Macao'), ('MN', 'Mongolia'), ('MH', 'Marshall Islands'), ('MK', 'Macedonia'), ('MU', 'Mauritius'), ('MT', 'Malta'), ('MW', 'Malawi'), ('MV', 'Maldives'), ('MQ', 'Martinique'), ('MP', 'Northern Mariana Islands'), ('MS', 'Montserrat'), ('MR', 'Mauritania'), ('IM', 'Isle of Man'), ('UG', 'Uganda'), ('TZ', 'Tanzania'), ('MY', 'Malaysia'), ('MX', 'Mexico'), ('IL', 'Israel'), ('FR', 'France'), ('AW', 'Aruba'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJ', 'Svalbard and Jan Mayen'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands  [Malvinas]'), ('FM', 'Micronesia (Federated States of)'), ('FO', 'Faroe Islands'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NA', 'Namibia'), ('VU', 'Vanuatu'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NZ', 'New Zealand'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('CK', 'Cook Islands'), ('CI', "C\xf4te d'Ivoire"), ('CH', 'Switzerland'), ('CO', 'Colombia'), ('CN', 'China'), ('CM', 'Cameroon'), ('CL', 'Chile'), ('CC', 'Cocos (Keeling) Islands'), ('CA', 'Canada'), ('CG', 'Congo'), ('CF', 'Central African Republic'), ('CD', 'Congo (the Democratic Republic of the)'), ('CZ', 'Czech Republic'), ('CY', 'Cyprus'), ('CX', 'Christmas Island'), ('CR', 'Costa Rica'), ('CW', 'Cura\xe7ao'), ('CV', 'Cabo Verde'), ('CU', 'Cuba'), ('SZ', 'Swaziland'), ('SY', 'Syria'), ('SX', 'Sint Maarten (Dutch part)'), ('KG', 'Kyrgyzstan'), ('KE', 'Kenya'), ('SS', 'South Sudan'), ('SR', 'Suriname'), ('KI', 'Kiribati'), ('KH', 'Cambodia'), ('SV', 'El Salvador'), ('KM', 'Comoros'), ('ST', 'Sao Tome and Principe'), ('SK', 'Slovakia'), ('KR', 'South Korea'), ('SI', 'Slovenia'), ('KP', 'North Korea'), ('KW', 'Kuwait'), ('SN', 'Senegal'), ('SM', 'San Marino'), ('SL', 'Sierra Leone'), ('SC', 'Seychelles'), ('KZ', 'Kazakhstan'), ('KY', 'Cayman Islands'), ('SG', 'Singapore'), ('SE', 'Sweden'), ('SD', 'Sudan'), ('DO', 'Dominican Republic'), ('DM', 'Dominica'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('VG', 'Virgin Islands (British)'), ('DE', 'Germany'), ('YE', 'Yemen'), ('DZ', 'Algeria'), ('US', 'United States of America'), ('UY', 'Uruguay'), ('YT', 'Mayotte'), ('UM', 'United States Minor Outlying Islands'), ('LB', 'Lebanon'), ('LC', 'Saint Lucia'), ('LA', 'Laos'), ('TV', 'Tuvalu'), ('TW', 'Taiwan'), ('TT', 'Trinidad and Tobago'), ('TR', 'Turkey'), ('LK', 'Sri Lanka'), ('LI', 'Liechtenstein'), ('LV', 'Latvia'), ('TO', 'Tonga'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('TH', 'Thailand'), ('TF', 'French Southern Territories'), ('TG', 'Togo'), ('TD', 'Chad'), ('TC', 'Turks and Caicos Islands'), ('LY', 'Libya'), ('VA', 'Holy See'), ('VC', 'Saint Vincent and the Grenadines'), ('AE', 'United Arab Emirates'), ('AD', 'Andorra'), ('AG', 'Antigua and Barbuda'), ('AF', 'Afghanistan'), ('AI', 'Anguilla'), ('VI', 'Virgin Islands (U.S.)'), ('IS', 'Iceland'), ('IR', 'Iran'), ('AM', 'Armenia'), ('AL', 'Albania'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AS', 'American Samoa'), ('AR', 'Argentina'), ('AU', 'Australia'), ('AT', 'Austria'), ('IO', 'British Indian Ocean Territory'), ('IN', 'India'), ('AX', '\xc5land Islands'), ('AZ', 'Azerbaijan'), ('IE', 'Ireland'), ('ID', 'Indonesia'), ('UA', 'Ukraine'), ('QA', 'Qatar'), ('MZ', 'Mozambique')], default='', max_length=2),
        ),
    ]
