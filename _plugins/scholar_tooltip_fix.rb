# frozen_string_literal: true

require "jekyll-socials"

module ScholarTooltipFix
  def render(context)
    super(context).gsub("title='Scholar userid'", "title='Scholar'")
  end
end

Jekyll::SocialLinksTag.prepend(ScholarTooltipFix)