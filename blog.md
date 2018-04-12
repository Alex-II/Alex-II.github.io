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
    <li>
        
    </li>
</ul>

## Research Papers Summary
<ul>
    <li>
        <a href="_research_summary/mapreduce.html">MapReduce: Simplified Data Processing on Large Clusters by Jeffrey Dean and Sanjay Ghemawa</a>
    </li>
</ul>


