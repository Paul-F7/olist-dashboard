import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


# Creates daily revenue chart lines
def create_revenue_chart(revenue_df):
    fig, ax = plt.subplots()
    ax.plot(revenue_df['date'], revenue_df['revenue'], 
            color='#1f77b4', linewidth=2)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Revenue (R$)', fontsize=12)
    ax.set_title('Daily Revenue', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

# Create daily orders line chart
def create_orders_chart(revenue_df):
    fig, ax = plt.subplots()
    ax.plot(revenue_df['date'], revenue_df['orders'], 
            color='#ff7f0e', linewidth=2)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Number of Orders', fontsize=12)
    ax.set_title('Daily Orders', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

# Create top categories bar chart
def create_categories_chart(categories_df, top_n=10):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    data = categories_df.head(top_n)
    bars = ax.bar(data['category'], data['revenue'], 
                   color=sns.color_palette('Blues_d', len(data)))
    
    ax.set_xlabel('Category', fontsize=12)
    ax.set_ylabel('Revenue (R$)', fontsize=12)
    ax.set_title(f'Top {top_n} Categories by Revenue', 
                 fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'R$ {height:,.0f}',
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    return fig

# Create delivery preformance bar chart
def create_delivery_chart(delivery_df, top_n=10):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    data = delivery_df.head(top_n)
    colors = sns.color_palette('Reds_r', len(data))
    bars = ax.barh(data['customer_state'], data['avg_delivery_days'], 
                    color=colors)
    
    ax.set_xlabel('Average Delivery Days', fontsize=12)
    ax.set_ylabel('State', fontsize=12)
    ax.set_title(f'Average Delivery Time by State (Top {top_n})', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
                f'{width:.1f} days',
                ha='left', va='center', fontsize=9, 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    return fig

# Create customer distribution bar chart
def create_customer_distribution_chart(state_summary, top_n=15):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    data = state_summary.head(top_n)
    bars = ax.bar(data['customer_state'], data['customers'],
                   color=sns.color_palette('Greens_d', len(data)))
    
    ax.set_xlabel('State', fontsize=12)
    ax.set_ylabel('Number of Customers', fontsize=12)
    ax.set_title(f'Top {top_n} States by Customer Count', 
                 fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig

# Create pie chart for category revenue distribution
def create_revenue_distribution(categories_df):
    fig, ax = plt.subplots(figsize=(10, 8))
    
    data = categories_df.head(8)
    colors = sns.color_palette('pastel')
    
    wedges, texts, autotexts = ax.pie(
        data['revenue'], 
        labels=data['category'],
        autopct='%1.1f%%',
        colors=colors,
        startangle=90
    )

    # Make percentage text bold
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    ax.set_title('Revenue Distribution by Category (Top 8)', 
                 fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig
