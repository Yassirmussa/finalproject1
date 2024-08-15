from rest_framework import serializers
from logic.models import Staff, Day, Allocation, Feedback
from datetime import datetime


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    Dayname = serializers.SerializerMethodField()
    class Meta:
        model = Day
        fields = '__all__'

    def get_Dayname(self, obj):
        return obj.get_Day_display()  # This will use the DAY_CHOICES to return the corresponding day name
    


class AllocationSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(source='Sid', read_only=True)
    day = DaySerializer(source='Did', read_only=True)
    class Meta:
        model = Allocation
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    allocation = AllocationSerializer(source='Aid', read_only=True)
    class Meta:
        model = Feedback
        fields = '__all__'

    def create(self, validated_data):
        # Get the current day (this will need to be adjusted based on your timezone or business logic)
        today = datetime.now().weekday() + 1  # Monday is 1, Sunday is 7
        
        # Fetch the Day object for today
        try:
            day = Day.objects.get(Day=today)
        except Day.DoesNotExist:
            raise serializers.ValidationError("Day for today does not exist in the database.")

        # Find the relevant Allocation for today (assuming there is a way to determine this)
        # You might need to adjust this based on your business logic
        allocation = Allocation.objects.filter(Did=day).first()  # or use appropriate filtering

        if not allocation:
            raise serializers.ValidationError("No allocation found for today.")

        # Create the Feedback object with the allocation
        feedback = Feedback.objects.create(Aid=allocation, **validated_data)
        return feedback