rails new ywlist3  
gem simple_form  
gem bootstrap-sass
***
gem devise  
rails g devise:install  
rails g devise User  
rails g devise:views
***
rails g scaffold list title:string content:text    
rake db:migrate
***
gem 'acts-as-taggable-on', '~> 3.4'  
rake acts_as_taggable_on_engine:install:migrations  
rake db:migrate
***
kaminari


















