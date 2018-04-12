---
layout: default
title: Blog
---

## Tech Blog
<ul>
  {% for post in site.posts %}
    {% if post.category == "tech" %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>

## Reading Notes
<ul>
  {% for post in site.posts %}
    {% if post.category == "notes" %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>

## Research Papers Summary
<ul>
  {% for post in site.posts %}
    {% if post.category == "papers" %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
