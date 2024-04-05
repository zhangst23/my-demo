class List < ActiveRecord::Base

	validates :title, presence: true,
                    length: { minimum: 5 }

    acts_as_taggable # Alias for acts_as_taggable_on :tags
  	acts_as_taggable_on :skills, :interests

  	
end
