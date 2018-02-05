---
layout: default2
title: Little Big Engineer
---


## [Tech Blog]({{ "tech_blog.html" | relative_url }})

<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>


## [Papers Summaries]({{ "papers_summaries.html" | relative_url }})
