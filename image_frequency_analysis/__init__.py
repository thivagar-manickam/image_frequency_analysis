from .frequency_analysis import FrequencyAnalysis


def image_frequency_analysis(
    image_name, filter_radius=80, high_pass_filter=False, low_pass_filter=False
):
    output = FrequencyAnalysis(
        image_path=image_name,
        filter_radius=filter_radius,
        high_pass_filter=high_pass_filter,
        low_pass_filter=low_pass_filter,
    )

    return output
