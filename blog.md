---
layout: default
title: Blog
---

## Research Papers Summaries
<ul>
  {% for post in site.posts %}
    {% if post.category == "papers" %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>

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

## Reading Notes, Talk Notes
Notes trying to capture the essence of talks or readings; nice for later review and occasionally with my own thoughts and interpreations.
<ul>
  {% for post in site.posts %}
    {% if post.category == "notes" %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>
