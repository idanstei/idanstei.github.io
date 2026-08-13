---
layout: page
permalink: /publications/
title: Publications
description: Selected publications, patents, and related work spanning medical imaging, acoustics, molecular imaging, and clinical translation.
nav: true
nav_order: 4
---

<!-- _pages/publications.md -->

Selected work is highlighted first. The remaining bibliography is organized by publication type and shown in reverse chronological order.

## Selected Publications

<div class="publications">

{% bibliography -f papers -q @*[selected=true] %}

</div>

## Peer-Reviewed Journal Articles

<div class="publications">

{% bibliography -f papers -q @article[selected!=true] %}

</div>

## Conference Papers & Abstracts

<div class="publications">

{% bibliography -f papers -q @inproceedings %}

</div>

## Patents

<div class="publications">

{% bibliography -f papers -q @misc %}

</div>

## Theses & Book Chapters

<div class="publications">

{% bibliography -f papers -q @phdthesis|@mastersthesis|@incollection %}

</div>

## Search All Entries

{% include bib_search.liquid %}
