---
layout: default
---


## Tech Blog

<ul>
  {% for post in site.posts limit 1 %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>



## [About]({{ "about.html" | relative_url }})



