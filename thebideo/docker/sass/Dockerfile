FROM ruby:latest
RUN gem install sass
WORKDIR /tmp
ENTRYPOINT ["sass", "--update", "/src:/dest"]