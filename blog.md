---
layout: default
title: Blog
---

## Tech Blog

<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

## Reading Notes

### [MapReduce: Simplified Data Processing on Large Clusters by Jeffrey Dean and Sanjay Ghemawa](research_summary/mapreduce.html)

## Research Papers Summary

### []()
