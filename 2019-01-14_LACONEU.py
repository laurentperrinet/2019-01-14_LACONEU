#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Evening Lectures: Demonstration of methods and techniques about computational neuroscience. Students will learn how to work analytically and by numerical simulations in biomedical applications.
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
DEBUG = True
DEBUG = False

import os
home = os.environ['HOME']
figpath_talk = 'figures'
figpath_slides = os.path.join(home, 'nextcloud/libs/slides.py/figures/')
# figpath_etienne = os.path.join(home, 'pool/EtienneRey')
# figpath_sparse = os.path.join(home, 'pool/science/Perrinet2015BICV_sparse/figures')
# figpath_bednar = os.path.join(home, 'pool/science/PerrinetBednar15/talk')
# figpath_bednar2 = os.path.join(home, 'pool/science/PerrinetBednar15/figures')
# figpath_méjanes = os.path.join(home, 'pool/blog/invibe/output/files/2016-04-28_méjanes/figures')
# figpath_FLE = os.path.join(home, 'ownCNRS/2018-03-26_cours-NeuroComp_FEP/figures')
#
# images_etienne = [         '2016_elasticite/photos/E-REY-TRAME_Elasticité-Vasarely.JPG',
#          '2018_TRAMES/files/2017-10-03_instabilité_N_pix=9449-R_dis=1.50-theta=29.00 deg-freq_A=0.07-R_dis_A=1.50-freq_B=0.03-R_dis_B=1.51-seuil_A=0.70-seuil_B=0.75-gain=10.00_render.png',
#          '2013_Tropique/photos/EtienneRey-Tropique-2011-C.JPG',
# ]
import sys
print(sys.argv)
tag = sys.argv[0].split('.')[0]
if len(sys.argv)>1:
    slides_filename = sys.argv[1]
else:
    slides_filename = None

print('😎 Welcome to the script generating the slides for ', tag)
YYYY = int(tag[:4])
MM = int(tag[5:7])
DD = int(tag[8:10])

# see https://github.com/laurentperrinet/slides.py
from slides import Slides

height_px = 80
height_ratio = .7

meta = dict(
 embed = True,
 draft = DEBUG, # show notes etc
 width= 1600,
 height= 1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin= 0.1618,#
 #  reveal_path = 'file://' + home + '/nextcloud/libs/slides.py/reveal.js/',
            # reveal_path = 'http://cdn.jsdelivr.net/reveal.js/3.0.0/',
 #reveal_path = 'https://s3.amazonaws.com/hakim-static/reveal-js/',
 #reveal_path = 'http://cdn.jsdelivr.net/reveal.js/3.0.0/',
 #reveal_path = 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.4.1/',
 reveal_path = 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/',
 #theme='night',
 #theme='sky',
 #theme='black',
 #theme='White',
 theme='simple',
 #theme='White',
 bgcolor = "white",
 author='Laurent Perrinet, INT',
 #author_link='Chloé Pasturel, Laurent Perrinet and Anna Montagnini',
 author_link='<a href="http://invibe.net">Laurent Perrinet</a>',
 short_title='Modelling spiking neural networks using Brian, Nest and pyNN',
 title='Modelling spiking neural networks using Brian, Nest and pyNN',
 conference_url='http://www.laconeu.cl',
 short_conference='LACONEU 2019',
 conference='LACONEU 2019: 5th Latin-American Summer School in Computational Neuroscience',
 location='Valparaiso (Chile)',
 YYYY = YYYY,
 MM = MM,
 DD = DD,
 tag = tag,
 url = 'http://invibe.net/LaurentPerrinet/Presentations/' + tag,
 abstract="""
""",
wiki_extras="""
----
<<Include(BibtexNote)>>
----
<<Include(AnrHorizontalV1Aknow)>>
----
TagYear{YY} TagTalks [[TagAnrHorizontalV1]]""".format(YY=str(YYYY)[-2:]),
 sections= ['Modelling SNNs',
            'Single cells',
            'Populations of cells',
            'Plasticity', ]
)

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

import pathlib
pathlib.Path(figpath_talk).mkdir(parents=True, exist_ok=True)

figname = os.path.join(figpath_talk, 'qr.png')
if not os.path.isfile(figname):
    import pyqrcode as pq
    code = pq.create(meta['url'])
    code.png(figname, scale=5)

print(meta['sections'])
s = Slides(meta)

#################################################################################
## 🏄🏄🏄🏄🏄🏄🏄🏄 intro  🏄🏄🏄🏄🏄🏄🏄🏄
#################################################################################
i_section = 0
s.open_section()
#################################################################################

s.hide_slide(content=s.content_figures(
    #[os.path.join(figpath_talk, 'qr.png')], bgcolor="black",
    [os.path.join(figpath_slides, 'mire.png')], bgcolor=meta['bgcolor'],
    height=s.meta['height']*.90),
    #image_fname=os.path.join(figpath_aSPEM, 'mire.png'),
    notes="""
Check-list:
-----------

* (before) bring miniDVI adaptors, AC plug, remote, pointer
* (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
* (VP) open monitor preferences / calibrate / title page
* (timer) start up timer
* (look) @ audience

http://pne.people.si.umich.edu/PDF/howtotalk.pdf

 """)

intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
# intro += s.content_figures(
# [os.path.join(figpath_aSPEM, "troislogos.png")], bgcolor="black",
# height=s.meta['height']*.2, width=s.meta['height']*.75)
intro += s.content_imagelet(os.path.join(figpath_slides, "troislogos.png"), s.meta['height']*.2) #bgcolor="black",
#intro += s.content_imagelet(os.path.join(figpath_talk, 'qr.png'), s.meta['height']*.2) #bgcolor="black",
# height=s.meta['height']*.2, width=s.meta['height']*.2)
#
intro += """
<h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>
""".format(**meta)
# intro += """
# <h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>
# {Acknowledgements}
# """.format(**meta)

s.add_slide(content=intro,
        notes="""
* (AUTHOR) Hi, I am Laurent Perrinet from (LOGO) the Institute de Neurosciences de la Timone in Marseille, a joint unit from the CNRS and AMU. Using computational models, I am investigating the link between the efficiency of behavioural responses in vision, their underlying neural code and their adaptation to the structure of the world.

* (SHOW TITLE - THEME) = mon but ici est de montrer quelques aspects de mon projet de recherche et en particulier des echos de ces tracaux que nous avons realiséavec Etienne Rey
please interrupt

""")



s.add_slide(content=s.content_figures([figname], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url= meta['url']),
notes=" All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")

s.add_slide(content=intro,
    notes="""
* (ACKNO) this endeavour involves different techniques, tools and... persons. From the head on, I wish to acknowledezg Chloe and Anna for doing most of this work +  thank the people who collaborated directly or indeirectly to this project and in particular Berk Mirza, Rick Adams and Karl Friston and the Wellcome Trust Centre for Neuroimaging for providing the tools for a successful visit and finally Jean-Bernard and Laurent Madelain for their essential knowledge in adaptation and reinforcement. C'est aussi le mentoring de Jean PEtitot quand j'était étudiant cogmaster ("DEA Sciences cognitives")

""")

# https://brian2.readthedocs.io/en/stable/_static/brian-logo.png
# http://www.nest-initiative.org/wp-content/uploads/2015/03/nest-initiative_logo.png
# http://neuralensemble.org/docs/PyNN/0.7/_static/pyNN_logo.png
s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "brian-logo.png"),
         os.path.join(figpath_talk, "nest-initiative_logo.png"),
         os.path.join(figpath_talk, "pyNN_logo.png"),], bgcolor="black",
        title=s.meta['title'], height=s.meta['height']*.6),
          notes="""

""")
s.close_section()

i_section += 1
#################################################################################
## 🏄🏄🏄🏄🏄🏄🏄🏄 Single cells - 15''  🏄🏄🏄🏄🏄🏄🏄🏄
#################################################################################
#################################################################################
s.open_section()
title = meta['sections'][i_section-1]
s.add_slide_outline(i_section-1)

s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "HH_Models.png"),], bgcolor="black",
        title=title, height=s.meta['height']*.6),
          notes="""
# ownCNRS/2019-01_LACONEU/2019-01-14_LACONEU/tmp/4-HH Models.ipynb

""")


s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "izhik.png"),], bgcolor="black",
        title=title, height=s.meta['height']*.6),
          notes="""

# https://www.izhikevich.org/publications/izhik.png

""")


s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "hugoladret_InternshipM2_CUBA.png"),], bgcolor="black",
        title=title, height=s.meta['height']*.6),
          notes="""

# https://github.com/hugoladret/InternshipM2/blob/master/FINAL_Retina_LGN_generation.ipynb

""")


s.close_section()

i_section += 1
#################################################################################
## 🏄🏄🏄🏄🏄🏄🏄🏄 Populations of cells - 15''  🏄🏄🏄🏄🏄🏄🏄🏄
#################################################################################
#################################################################################

s.open_section()
title = meta['sections'][i_section-1]
s.add_slide_outline(i_section-1)
s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "Fig_ring_model.png"),], bgcolor="black",
        title=title, height=s.meta['height']*.6),
          notes="""

# /Volumes/data/2018_backup/archives/2018_science/2018_HL_M1/figs/Fig_ring_model.pdf
#

""")


for figname in [ 'Brunel200Fig1.png', 'Brunel200Fig2.png']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, figname),], bgcolor="black",
        title=title, height=s.meta['height']*.6),
          notes="""


# https://sci-hub.tw/https://doi.org/10.1016/S0925-2312(00)00179-X

""")

s.close_section()

i_section += 1
#################################################################################
## 🏄🏄🏄🏄🏄🏄🏄🏄 STDP - 15''  🏄🏄🏄🏄🏄🏄🏄🏄
#################################################################################
#################################################################################

s.open_section()
title = meta['sections'][i_section-1]
s.add_slide_outline(i_section-1)
s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "fig_sup_stdps.png"),], bgcolor="black",
        title=title, height=s.meta['height']*.6),
          notes="""

#  /Users/laurentperrinet/nextcloud/RTC/2019-01-11\ rapport\ M2A\ HL\ 5bf69490a5705a15960895d6/Figures/fig_sup_stdps.pdf

""")

s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, "hugoladret_InternshipM2_FINAL_1_couche.png"),], bgcolor="black",
        title=s.meta['title'], height=s.meta['height']*.6),
          notes="""

# https://github.com/hugoladret/InternshipM2/blob/master/FINAL_1_couche.ipynb

""")


# FINAL_L2_noshift.pdf
s.close_section()

#################################################################################
## 🏄🏄🏄🏄🏄🏄🏄🏄 OUTRO - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
#################################################################################
#################################################################################
s.open_section()
s.add_slide(content=intro,
    notes="""
* Thanks for your attention!
""")
s.close_section()


if slides_filename is None:

    with open("/tmp/wiki.txt", "w") as text_file:
        text_file.write("""\
#acl All:read

= {title}  =

 Quoi:: [[{conference_url}|{conference}]]
 Qui:: {author}
 Quand:: {DD}/{MM}/{YYYY}
 Où:: {location}
 Support visuel:: http://blog.invibe.net/files/{tag}.html


 What:: talk @ the [[{conference_url}|{conference}]]
 Who:: {author}
 When:: {DD}/{MM}/{YYYY}
 Where:: {location}
 Slides:: http://blog.invibe.net/files/{tag}.html

== reference ==
{{{{{{
#!bibtex
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}, {location}",
    Title = "{title}",
    Url = "{url}",
    Year = "{YYYY}",
}}
}}}}}}
## add an horizontal rule to end the include
{wiki_extras}
""".format(**meta) )

else:
    s.compile(filename=slides_filename)

# Check-list:
# -----------
#
# * (before) bring miniDVI adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# Preparing Effective Presentations
# ---------------------------------
#
# Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.
#
# Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.
#
# Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.
#
# Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.
#
# Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.
#
# Unified - An image is most effective when information is organized around a single central theme and tells a unified story.
#
# Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.
#
# Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.
#
# Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.
#
# Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.
#
# Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.
#
# Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.
#
# Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
